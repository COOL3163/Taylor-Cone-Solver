"""Streamlit demonstration app for Taylor-Cone Solver.

Simple demonstration interface for presentations and quick testing.
"""

import sys
from pathlib import Path

import streamlit as st

# Add the package root to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solver"))

from solver.app_backend import (
    RunParams,
    run_solver,
    figure_field_magnitude,
    figure_potential,
)

# Set page config
st.set_page_config(
    page_title="Taylor-Cone Solver Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS for clean presentation
st.markdown("""
<style>
    .big-title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 30px;
        color: #1f77b4;
    }
    .subtitle {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 50px;
        color: #555;
    }
    .team-info {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Main navigation
demo_mode = st.sidebar.radio(
    "Presentation Section",
    ["1️⃣ Introduction (Curtis)", "2️⃣ Theory & App (Ethan)", "3️⃣ Results (Li Ang)"],
    index=0
)

st.sidebar.divider()

# ============================================================================
# SECTION 1: CURTIS - INTRODUCTION (0:00-0:25)
# ============================================================================
if demo_mode == "1️⃣ Introduction (Curtis)":
    # Header
st.markdown('<div class="big-title">Taylor-Cone Electrostatic-Capillary Solver</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A Lightweight Framework for Electrospray Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="team-info">Rui Xuan Ethan Yang, Li Ang Dong, Wai Ip Curtis Lau</div>', unsafe_allow_html=True)

    st.divider()

    # Two-column layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("What is a Taylor Cone?")
        st.write("""
        An electric field can pull a conducting liquid into a pointed shape called a **Taylor cone**.

        The ideal theory predicts a half-angle of about **49.3 degrees**.

        **Our research question:**
        Can a computer model reliably identify this angle—and can different cone shapes produce equally convincing results?
        """)

        # Display system schematic
        schematic_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "system_schematic.png"
        if schematic_path.exists():
            st.image(str(schematic_path), caption="Taylor cone schematic", use_container_width=True)

    with col2:
        st.subheader("Force Balance")
        st.write("""
        Two competing forces shape the cone:

        - **Electric pressure** (Maxwell stress) pulls the liquid outward
        - **Surface tension** (capillary pressure) resists deformation

        At equilibrium, these forces balance to create the characteristic cone shape.
        """)

        # Display geometry diagram
        geom_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "geometry.png"
        if geom_path.exists():
            st.image(str(geom_path), caption="Force diagram", use_container_width=True)

# ============================================================================
# SECTION 2: ETHAN - THEORY AND APP DEMONSTRATION (0:25-1:15)
# ============================================================================
elif demo_mode == "2️⃣ Theory & App (Ethan)":
    st.title("⚡ Theory and Application Demonstration")

    st.write("""
    **Electric pressure** pulls on the liquid surface, while **surface tension** resists deformation.

    Our model assumes the cone is **stationary** and **symmetric** around its axis.
    For each candidate shape, we calculate the surrounding electric field.
    """)

    st.divider()

    # Theory explanation
    with st.expander("📐 Two Methods for Identifying the Taylor Angle", expanded=True):
        st.write("""
        We compare two methods:

        1. **Pressure Balance Method**: Finds the smallest mismatch between electric and capillary pressure,
           after fitting a pressure offset and field amplitude.

        2. **Field Decay Method**: Measures how the squared surface field changes with distance from the cone's virtual tip.
           An ideal Taylor solution follows an inverse-distance relationship.
        """)

    st.divider()

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Solver Settings")

        st.subheader("Geometry")
        electrode_spacing = st.number_input("Electrode spacing [mm]", value=3.0, step=0.1) * 1e-3
        nozzle_radius = st.number_input("Domain radius [mm]", value=2.0, step=0.1) * 1e-3

        st.subheader("Physics")
        V0 = st.number_input("Applied voltage [kV]", value=2.5, step=0.1) * 1000.0
        gamma = st.number_input("Surface tension [mN/m]", value=22.0, step=0.5) * 1e-3

        st.subheader("Mesh")
        grid_quality = st.select_slider("Grid quality", options=["Coarse", "Medium", "Fine"], value="Medium")
        grid_map = {"Coarse": (41, 61), "Medium": (61, 89), "Fine": (81, 121)}
        nr, nz = grid_map[grid_quality]

        st.subheader("Interface")
        interface_angle = st.slider("Cone half-angle [°]", 40.0, 55.0, 49.3, 0.1)

    # Main content
    st.subheader("🖥️ Application Interface")
    st.write(f"""
    **Current settings:**
    - Geometry: {electrode_spacing*1e3:.1f} mm spacing, {nozzle_radius*1e3:.1f} mm radius
    - Physics: {V0/1000:.2f} kV applied, {gamma*1e3:.1f} mN/m surface tension
    - Grid: {nr} × {nz} cells ({grid_quality})
    - Test angle: {interface_angle:.1f}°
    """)

    if st.button("▶️ Run Calculation", type="primary"):
        with st.spinner("Computing electric field..."):
            params = RunParams(
                V0=V0,
                gamma=gamma,
                electrode_spacing=electrode_spacing,
                nozzle_radius=nozzle_radius,
                nr=nr,
                nz=nz,
                space_charge_model="none",
                interface_half_angle_deg=interface_angle,
            )

            try:
                result = run_solver(params)
                st.session_state.demo_result = result
                st.session_state.demo_params = params
                st.success(f"✅ Calculation complete! Runtime: {result.runtime_s:.2f} s")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    # Display precomputed results
    if "demo_result" in st.session_state:
        result = st.session_state.demo_result

        st.divider()
        st.subheader("📊 Field Visualization")

        col1, col2 = st.columns(2)

        with col1:
            fig_pot = figure_potential(result)
            fig_pot.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_pot, use_container_width=True)
            st.caption("**Potential field** φ(r,z) - Emitter at top (V₀), ground at bottom")

        with col2:
            fig_field = figure_field_magnitude(result)
            fig_field.update_layout(height=500, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_field, use_container_width=True)
            st.caption("**Field magnitude** |E| - Peak field at cone apex")

        # Key metrics
        st.divider()
        met1, met2, met3, met4 = st.columns(4)
        met1.metric("Interface angle", f"{result.half_angle:.2f}°")
        met2.metric("Peak field", f"{result.peak_field:.2e} V/m")
        met3.metric("RMS residual", f"{result.rms_residual:.2e} Pa")
        met4.metric("Runtime", f"{result.runtime_s:.2f} s")
    else:
        st.info("👆 Click **Run Calculation** above to compute the field and see results.")

# ============================================================================
# SECTION 3: LI ANG - RESULTS AND LIMITATIONS (1:15-2:00)
# ============================================================================
else:  # Li Ang section
    st.title("📈 Results and Limitations")

    st.write("""
    We tested both methods across different cone angles and boundary conditions.

    These are **previously computed results** from our verification studies.
    """)

    st.divider()

    # Key findings
    st.subheader("🔍 Key Findings")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Method 1: Pressure Balance")
        st.warning("""
        **Different cone shapes produced comparably small stress mismatches.**

        Thus, the first method **did not identify a unique angle**.

        This reveals a fundamental ambiguity in parameter fitting.
        """)

        # Show multistart plot
        multistart_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "05_optimizer_multistart.png"
        if multistart_path.exists():
            st.image(str(multistart_path), caption="Multiple angles produce similar residuals", use_container_width=True)

    with col2:
        st.markdown("#### Method 2: Field Decay")
        st.success("""
        **With ideal Taylor conditions** imposed at the outer boundary:
        - Recovered angles: **49.07° to 49.25°**
        - Close to theoretical 49.3°

        **With grounded outer boundary:**
        - Found **no crossing**
        - Returned **no angle**
        """)

        # Show exponent crossing plot
        crossing_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "exponent_crossing.png"
        if crossing_path.exists():
            st.image(str(crossing_path), caption="Field decay identifies angle with Taylor BC", use_container_width=True)

    st.divider()

    # Verification results
    st.subheader("✅ What We Verified")

    ver_col1, ver_col2, ver_col3 = st.columns(3)

    with ver_col1:
        st.metric("Convergence Order", "≈ 2nd order", help="Regular Poisson problem")
        st.caption("Manufactured solution test")

    with ver_col2:
        st.metric("FEM Agreement", "0.024%", help="Potential difference at finest grid")
        st.caption("Independent verification")

    with ver_col3:
        st.metric("Angle Recovery", "49.14° - 49.20°", help="With Taylor boundary conditions")
        st.caption("Classical benchmark")

    st.divider()

    # Limitations
    st.subheader("⚠️ Scope and Limitations")

    st.error("""
    **What we did NOT do:**

    - ❌ **No physical experiments** - We conducted no laboratory validation
    - ❌ **No liquid motion** - Model excludes fluid dynamics
    - ❌ **Partial solver testing** - Numerical tests checked components, not the full physical model

    **Main result:**

    The **boundary conditions** affect whether an angle can be identified.

    Recovering 49.3° checks **agreement with the imposed ideal conditions**—it does not independently predict the shape of a real liquid cone.
    """)

    st.divider()

    # Conclusion
    st.subheader("🎯 Conclusion")

    st.info("""
    **Our claim:**

    We created a **transparent, low-cost computational bridge** between field calculations and cone measurements.

    This framework can help researchers:
    - Explore designs
    - Diagnose model behavior
    - Decide what measurements are needed next

    **Not a claim:**
    - We have NOT replaced full multiphysics simulation
    - We have NOT completed laboratory validation
    - We do NOT independently predict the physical cone shape
    """)

    # Show comparison figures
    st.divider()
    st.subheader("📸 Supporting Evidence")

    comp_col1, comp_col2 = st.columns(2)

    with comp_col1:
        fem_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "01_regular_poisson_fem.png"
        if fem_path.exists():
            st.image(str(fem_path), caption="FEM comparison - sub-percent agreement", use_container_width=True)

    with comp_col2:
        sensitivity_path = Path(__file__).resolve().parents[1] / "paper_submission" / "figures" / "04_sensitivity_landscapes.png"
        if sensitivity_path.exists():
            st.image(str(sensitivity_path), caption="Parameter sensitivity analysis", use_container_width=True)

# Footer
st.divider()
st.caption("Taylor-Cone Solver Demo | Rui Xuan Ethan Yang, Li Ang Dong, Wai Ip Curtis Lau")
