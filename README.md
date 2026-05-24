# Where Institutions Fail, Stress Becomes Repression

A path-weighted framework for anticipating societal trajectories.

**Authors:** Hyun Ho Jung (KAIST Graduate School of Future Strategy)
**Status:** Manuscript submitted to *Nature Human Behaviour* (2026)
**Version:** v0.4 (2026-05-25)
**Zenodo DOI:** https://doi.org/10.5281/zenodo.20370479 (Concept DOI — always latest)

---

## Summary

Across 93 countries from 2000 to 2022, we show that civil liberties repression responds to institutional resilience more than 2.5 times as strongly as it responds to social stress itself. A path-weighted action functional, inspired by the path-integral formalism of statistical mechanics but anchored in standard cross-national econometrics, accounts for 77% of cross-national variance.

**Key result:** α (stress) = 0.63 [0.53, 0.73], **β (institutional resilience) = 1.67 [1.59, 1.74]**, η (future expectation) = 0.73 [0.66, 0.81]; R² = 0.77; N = 2,136 country-year observations.

## Repository structure

```
.
├── README.md                — This file
├── LICENSE                   — MIT
├── CITATION.cff              — How to cite
├── requirements.txt          — Python dependencies
├── .gitignore                — Standard Python + data exclusions
├── code/                     — Analysis pipeline (Python)
│   ├── 01_data_collection.py        — World Bank panel construction
│   ├── 02_vdem_processing.py        — V-Dem E variable synthesis
│   ├── 03_panel_expansion_estimation.py — 93-country OLS·FE·Bootstrap
│   └── 04_figures.py                — NHB-quality figures
├── data/                     — Processed analytical panels
│   ├── panel_100.csv         — Primary: 93 countries, 2000–2022, N=2,136
│   └── panel_29.csv          — Robustness: 29 countries with most complete coverage
├── figures/                  — Manuscript figures (300 DPI)
├── manuscript/               — Draft + abstract + cover letter
└── docs/                     — Replication instructions
```

## Reproducing the analysis

### Requirements
- Python ≥ 3.10
- See `requirements.txt`

### Steps

```bash
# 1. Install
pip install -r requirements.txt

# 2. Download V-Dem v16 (one-time, ~400MB)
#    Register at https://v-dem.net → download CY-Full+Others-v16 CSV
#    Place in: data/vdem/V-Dem-CY-Full+Others-v16.csv

# 3. Run the pipeline (each script outputs to data/ and figures/)
python code/01_data_collection.py       # World Bank panel (~5 min, API)
python code/02_vdem_processing.py       # V-Dem E variable (~1 min)
python code/03_panel_expansion_estimation.py  # 93-country estimation
python code/04_figures.py               # Figure 1·2·3
```

Expected output:
- `data/panel_100.csv` (2,136 country-year observations)
- `figures/Figure_1_three_coefficients.png`
- `figures/Figure_2_Korea_trajectory.png`
- `figures/Figure_3_beta_dominance.png`
- Console: α=0.63, β=1.67, η=0.73, R²=0.77

## Data sources

- **V-Dem v16** (Coppedge et al., 2024) — Varieties of Democracy. https://v-dem.net (CC-BY 4.0)
- **World Development Indicators** (World Bank, 2024) — https://databank.worldbank.org (CC-BY 4.0)
- **Korean fertility indicators** (Statistics Korea, KOSIS) — https://kosis.kr

## Citation

If you use this code or data, please cite:

```bibtex
@article{Jung2026PathWeighted,
  author  = {Jung, Hyun Ho},
  title   = {Where institutions fail, stress becomes repression: A path-weighted framework for anticipating societal trajectories},
  journal = {Nature Human Behaviour},
  year    = {2026},
  note    = {Under review}
}
```

Replication archive (data + code with DOI):
- Zenodo: https://doi.org/10.5281/zenodo.20370479 (Concept DOI) · https://doi.org/10.5281/zenodo.20370480 (v1)
- This GitHub repository: https://github.com/Chunghyunho/spim-nhb-2026

## Companion work

A full empirical Article extending the panel to 1960–2022 and incorporating three Korean natural experiments (1997 financial crisis, 2016–17 presidential impeachment, 2020–24 demographic shock) is in preparation. Pre-registration of falsifiable predictions F3–F5 is planned for submission alongside.

## Acknowledgments

This work uses data made publicly available by the Varieties of Democracy (V-Dem) Institute, the World Bank, and Statistics Korea. Advisor: Prof. Yong-Seok Seo (KAIST Graduate School of Future Strategy).

## License

Code: MIT (see LICENSE). Data: as licensed by original providers (V-Dem CC-BY 4.0; World Bank CC-BY 4.0).
