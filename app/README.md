# Taylor-Cone Solver Streamlit Application

Professional interactive interface for the Taylor-cone electrostatic-capillary solver.

## Overview

This application provides an interactive, publication-quality interface for:
- Electrostatic field computation (Laplace/Poisson)
- Young-Laplace-Maxwell residual analysis
- Onset voltage prediction
- Immersed boundary verification
- Space-charge shielding models

## Quick Start

### Run the Application

```bash
streamlit run app/streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Legacy Application

The previous single-file app is preserved as `streamlit_app_legacy.py` and can be run with:

```bash
streamlit run app/streamlit_app_legacy.py
```

## Application Structure

```
app/
├── streamlit_app.py              # Main entry point with navigation
├── streamlit_app_legacy.py       # Original single-file app (preserved)
├── app_pages/                    # Multi-page application
│   ├── 01_overview.py           # Landing page with theory
│   ├── 02_solver.py             # Main solver interface
│   ├── 03_verification.py       # Immersed boundary verification
│   └── 07_documentation.py      # Theory and methods reference
├── components/                   # Reusable UI components
│   ├── parameter_panel.py       # Parameter input widgets with presets
│   ├── plot_styling.py          # Academic plot styling
│   └── theory_boxes.py          # Mathematical theory boxes
├── .streamlit/
│   └── config.toml              # Theme configuration (academic style)
├── assets/
│   └── presets/                 # JSON parameter presets
│       ├── ethanol_standard.json
│       ├── water_standard.json
│       └── formamide_standard.json
└── docs/
    └── SCIENTIST_USER_GUIDE.md  # Detailed guide for scientists
```

## Features

### Professional Design
- Academic color scheme (serif fonts, blue accents)
- Generous spacing for plots (550-600px height)
- Publication-quality figure styling
- Material Symbols icons throughout

### Parameter Management
- **Presets:** Load validated configurations from literature
- **Hierarchical organization:** Geometry, Materials, Physics, Mesh, Solver Settings
- **Validation:** Real-time parameter checking with warnings
- **Documentation:** Inline tooltips and theory boxes

### Visualization
- Enhanced spacing for all plots (side-by-side with spacers)
- Academic styling (white background, professional colormaps)
- Interactive Plotly charts with zoom, pan, hover
- Export-ready figures

### Results Management
- Run history tracking in session state
- Results exported to `results/`
- JSON export for programmatic analysis
- Copyable parameter summaries

### Verification Suite
- Taylor angle recovery (→ 49.29°)
- Taylor identity test (V₀*/A* ≈ 1.000)
- Grid convergence visualization
- Flank field exponent landscape

## Usage Workflows

### 1. Basic Solver Run

1. Navigate to **Solver** tab
2. Select a preset (e.g., "Ethanol (standard)")
3. Click **▶️ Run Solver**
4. Examine scalar diagnostics and field plots
5. Export results if needed

### 2. Onset Voltage Prediction

1. Set your fluid's surface tension and geometry
2. Start with Taylor angle (49.3°)
3. Run solver at guessed voltage
4. Examine RMS residual:
   - Residual ≈ 0 → voltage is near onset
   - Residual large → adjust voltage and rerun

### 3. Verification

1. Navigate to **Verification** tab
2. Select Fine or Very Fine grid
3. Click **▶️ Run Verification**
4. Check recovered angle (should be ≈49.2°)
5. Check identity ratio (should be ≈1.000)

## Parameter Reference

### Quick Defaults (Ethanol, Standard)

```python
gamma = 22 mN/m              # Surface tension
electrode_spacing = 10 mm    # Domain height
nozzle_radius = 10 mm       # Domain width
V0 = 2.5 kV                 # Applied voltage
space_charge_model = none   # Vacuum electrostatics
interface_angle = 49.3°     # Taylor angle
grid = 31 × 51              # Medium resolution
```

### Expected Runtime

- **Coarse grid (21×31):** < 0.5 seconds
- **Medium grid (31×51):** ~0.5–1 seconds
- **Fine grid (41×71):** ~1–2 seconds
- **Verification (Fine 121×177):** ~10–30 seconds

## Troubleshooting

### App doesn't start
- Check that you're running from the repository root
- Verify all dependencies installed: `pip install -e ".[app]"`
- Try legacy app to isolate issue: `streamlit run app/streamlit_app_legacy.py`

### Import errors
- The app pages add the package root (`solver/`) to `sys.path` for imports
- Verify `app_backend.py` exists in `solver/solver/`
- Alternatively install the package: `pip install -e .`

### Plots not displaying
- Check that solver runs complete without exceptions
- Verify Plotly installed: `pip install plotly`
- Try clearing cache with **🗑️ Clear Cache** button

### Solver doesn't converge
- Reduce under-relaxation ω (try 0.3 or 0.2)
- Increase max iterations
- Check space-charge parameters are physical
- Use coarser grid for initial exploration

### Verification angle far from 49.29°
- Use Fine or Very Fine grid (coarse grids have ~1° error)
- Verify Taylor far-field BC is being used
- Check that domain is square (electrode_spacing ≈ nozzle_radius)

## Design Philosophy

This application follows professional scientific software design principles:

1. **Professional appearance** with academic color schemes and typography
2. **Clear hierarchy** from problem setup → solve → analysis → export
3. **Self-documenting** with integrated theory and parameter tooltips
4. **Research-ready** outputs suitable for papers and presentations
5. **Educational** with guided workflows and explanatory text

## Citation

If you use this application in your research, please cite:

```bibtex
@software{yang2026taylor,
  title={Taylor-Cone Electrostatic-Capillary Solver},
  author={Yang, Rui Xuan Ethan and Dong, Li Ang and Lau, Wai Ip Curtis},
  year={2026},
  institution={Independent Schools Foundation Academy},
  address={Hong Kong SAR},
  url={https://github.com/eyang8216/taylor-cone-solver}
}
```

## License

Open-source educational research project. See repository root for details.
