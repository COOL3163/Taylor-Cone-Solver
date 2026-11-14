# Taylor-Cone Electrospray Solver

A reduced-order axisymmetric electrostatic-capillary solver for Taylor-cone modeling, electrospray applications, and colloid thruster design.

---

## About This Project

This is a **one-time upload** of our research project, cleaned and prepared for professional use. The project was developed by middle school students at Independent Schools Foundation Academy. While we have implemented rigorous verification and testing, there may be fundamental technical issues we have overlooked. Users are advised to validate results against experimental data or other established methods for critical applications.

**AI Disclosure:** AI tools were used to generate the user interface based on testing code, assist with LaTeX debugging and styling, debug the codebase (approximately 5% of all written code), and write this README documentation.

---

## Overview

This repository provides a complete numerical framework for solving the coupled electrostatic-capillary problem at the heart of electrospray phenomena. The solver uses finite-difference methods with immersed boundary techniques to model the iconic Taylor cone—the pointed interface that forms when electric stress balances surface tension.

**Key Capabilities:**
- Axisymmetric Laplace/Poisson electrostatics with immersed boundaries
- Young-Laplace-Maxwell force balance computation
- Onset voltage prediction via amplitude projection
- Optional space-charge shielding models
- Interactive Streamlit application
- 84 automated tests with verification studies

**Scientific Foundation:** The solver implements the classical Taylor (1964) theory for electrohydrodynamic cone formation, verified against the theoretical 49.29° half-angle.

---

## Repository Structure

```
taylor-cone-solver/
├── solver/              # Core Python package
│   ├── solver/          # Package modules
│   │   ├── grid.py               # Axisymmetric grid generation
│   │   ├── operators.py          # Finite-difference operators
│   │   ├── electrostatics.py    # Laplace/Poisson solvers
│   │   ├── immersed_boundary.py # White-exact stencils
│   │   ├── interface.py          # Young-Laplace-Maxwell balance
│   │   └── optimization.py       # Shape optimization (experimental)
│   ├── experimental/    # Imaging toolkit and synthetic validation
│   ├── tests/           # 84 automated tests
│   └── examples/        # 12 demonstration scripts
├── app/                 # Streamlit interactive application
│   ├── streamlit_app.py          # Main entry point
│   ├── app_pages/                # Multi-page interface
│   ├── components/               # Reusable UI components
│   └── docs/                     # User guides
├── paper_submission/    # Research paper (LaTeX)
│   ├── main.tex                  # Main document
│   ├── sections/                 # Paper sections
│   ├── figures/                  # Generated figures
│   └── references.bib            # Bibliography
├── results/             # Solver outputs and data
├── pyproject.toml       # Package configuration
└── requirements.txt     # Dependencies
```

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/eyang8216/taylor-cone-solver.git
cd taylor-cone-solver

# Install the package
pip install -e ".[imaging,app]"    # Optional extras: imaging toolkit, Streamlit app
```

The package can also be used without installing by setting `PYTHONPATH=solver`.

### Run Tests

```bash
python -m pytest
```

All 84 tests should pass, including:
- Grid generation and operator accuracy
- Electrostatic solver convergence
- Immersed boundary stencil verification
- Taylor angle recovery (→ 49.29°)
- Amplitude identity tests

### Run an Example

```bash
PYTHONPATH=solver python solver/examples/07_immersed_free_boundary.py
```

Available examples (in `solver/examples/`):
- `00_poisson_convergence.py` - Quartic manufactured solution
- `01_axisymmetric_laplace.py` - Basic field solver
- `02_simple_cone_laplace.py` - Fixed cone geometry
- `07_immersed_free_boundary.py` - Full free-boundary solve
- `10_quartic_poisson_convergence.py` - Convergence study
- And more...

### Run the Interactive App

```bash
streamlit run app/streamlit_app.py
```

The app provides:
- **Solver Tab:** Interactive parameter control with fluid presets
- **Verification Tab:** Taylor angle recovery and grid convergence
- **Documentation Tab:** Integrated theory and method references
- **Professional Styling:** Publication-quality plots and academic design

See [app/README.md](app/README.md) for detailed usage instructions.

### Compile the Paper

```bash
cd paper_submission
latexmk -pdf main.tex
```

The paper provides complete theoretical derivations, numerical implementation details, verification results, and validation against published experimental images.

---

## Scientific Results

### V3 Immersed Free-Boundary Milestone

The solver successfully:

✅ **Recovers the Taylor angle** - Computes 49.14° to 49.20° (theory: 49.29°) with immersed boundaries  
✅ **Verifies amplitude identity** - Taylor's V₀*/A* ratio within 1% of unity (1.0005–1.0069)  
✅ **Predicts onset voltage** - V₀* ≈ 2.8–3.0 kV for millimeter-scale ethanol (matches literature)  
✅ **Demonstrates convergence** - Immersed operator shows systematic refinement (10.33 → 4.26 → 2.55 V interface change)  
✅ **Passes manufactured tests** - Quartic Poisson convergence and cubic-exact field reconstruction  

### Key Findings

- **Immersed Boundary Accuracy:** Interface potential change improves systematically under refinement (staircase baseline does not)
- **Onset Diagnostic Limitation:** Amplitude-projected residual minimum is grid-dependent; exponent crossing shows promise as a more robust identifier
- **Classical Benchmark:** Reproduces the ideal 49.29° half-angle to within 0.16° across three refinement levels
- **Space-Charge Effects:** Positive apex-local shielding metric (~1.3%) for Gaussian closure

---

## Documentation

### For Users
- **[README.md](README.md)** (this file) - Quick start and overview
- **[app/README.md](app/README.md)** - Streamlit app usage guide
- **[app/docs/SCIENTIST_USER_GUIDE.md](app/docs/SCIENTIST_USER_GUIDE.md)** - Scientific workflows and interpretation
- **[paper_submission/main.pdf](paper_submission/main.pdf)** - Complete research paper

### For Developers
- **[solver/tests/](solver/tests/)** - Test suite with examples of API usage
- **[solver/examples/](solver/examples/)** - Demonstration scripts
- **Module docstrings** - Inline documentation in all solver modules

---

## Authors and Affiliation

**Rui Xuan Ethan Yang, Li Ang Dong, Wai Ip Curtis Lau**

Independent Schools Foundation Academy, Hong Kong SAR

**Contact:**
- Rui Xuan Ethan Yang: eyang8216@gmail.com
- Li Ang Dong: elliott.dong3015002@gmail.com
- Wai Ip Curtis Lau: cwilau09@gmail.com

**Work Contribution:**
- All three authors jointly conceived the project idea
- Rui Xuan Ethan Yang built the repository structure, wrote and derived all theoretical foundations
- Rui Xuan Ethan Yang and Li Ang Dong completed the codebase and verification suite
- Rui Xuan Ethan Yang, Li Ang Dong, and Wai Ip Curtis Lau jointly wrote the research paper

**Note:** This project was developed by middle school students as a one-time upload cleaned for professional use. There may be fundamental technical issues we have overlooked. User discretion is advised.

---

## Citation

If you use this solver in your research, please cite:

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

Please also acknowledge the original Taylor (1964) theory:

```bibtex
@article{taylor1964disintegration,
  title={Disintegration of water drops in an electric field},
  author={Taylor, Geoffrey Ingram},
  journal={Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences},
  volume={280},
  number={1382},
  pages={383--397},
  year={1964},
  publisher={The Royal Society London}
}
```

---

## Applications

This solver is designed for:

- **Electrospray Research:** Modeling the onset and shape of Taylor cones in electrospray ionization mass spectrometry (ESI-MS)
- **Colloid Thrusters:** Predicting operating voltages and cone angles for spacecraft propulsion
- **Electrohydrodynamics:** Studying electric-field-driven interface deformation
- **Educational Use:** Teaching coupled physics problems and numerical methods

---

## Technical Highlights

### Numerical Methods
- **Finite Differences:** Second-order accurate on stretched cylindrical grids
- **Immersed Boundaries:** White-exact cubic interpolation for curved interfaces
- **Iterative Solvers:** Gauss-Seidel with successive over-relaxation (SOR)
- **Field Reconstruction:** One-sided cubic stencils for normal electric field

### Verification Strategy
- **Manufactured Solutions:** Quartic Poisson convergence demonstrates solver accuracy
- **Analytical Limits:** Taylor far-field boundary conditions recover classical 49.29° angle
- **Grid Convergence:** Systematic refinement studies confirm discretization error decay
- **Baseline Comparisons:** Staircase grid used as negative control for immersed methods

### Software Engineering
- **84 Tests:** Comprehensive pytest suite with fixtures and parameterized tests
- **Type Hints:** Full type annotations for clarity and IDE support
- **Modular Design:** Clean separation of grid, operators, physics, and optimization
- **Reproducibility:** Pinned dependencies and example scripts with known outputs

---

## Current Limitations

- **2D Axisymmetric Only:** Full 3D cone perturbations not modeled
- **Single Interface:** Multi-jet and droplet emission not supported
- **Steady State:** Time-dependent dynamics not implemented
- **Experimental Validation:** Physical apparatus validation planned but not yet conducted

See the paper's Limitations section for detailed discussion.

---

## Contributing

This is an open-source educational research project. Contributions, bug reports, and suggestions are welcome via GitHub issues and pull requests.

**Areas for Extension:**
- Time-dependent solver for jet dynamics
- Multi-jet and droplet breakup models
- Experimental validation with high-speed imaging
- GPU acceleration for large-scale simulations
- Extended constitutive models (viscoelastic fluids, ion transport)

---

## License

Open-source educational research project. Free to use and modify with attribution.

---

## Authors

**Rui Xuan Ethan Yang, Li Ang Dong, Wai Ip Curtis Lau**

Independent Schools Foundation Academy, Hong Kong SAR

**Contact:**
- Rui Xuan Ethan Yang: eyang8216@gmail.com
- Li Ang Dong: elliott.dong3015002@gmail.com
- Wai Ip Curtis Lau: cwilau09@gmail.com

For questions or collaboration inquiries, please open a GitHub issue or contact the authors directly.

---

## Acknowledgments

This work builds on the foundational electrohydrodynamic theory of Sir Geoffrey Ingram Taylor and the extensive experimental literature on electrospray phenomena. We thank the open-source scientific Python community for the tools that made this work possible.
