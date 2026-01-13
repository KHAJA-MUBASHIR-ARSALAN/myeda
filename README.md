# myeda
Build a light weight library for eda.



MYEDA

myeda is a lightweight, fast Exploratory Data Analysis (EDA) library for pandas DataFrames.

It is designed for developers and data scientists who want quick insights without heavy dependencies, auto-generated HTML reports, or slow dashboards.

WHY MYEDA

Lightweight and fast

Minimal dependencies

Explicit function calls (no magic)

Modular design

Suitable for large datasets

PyPI-published and test-covered

This library intentionally avoids:

Auto HTML reports

Heavy visualization frameworks

Hidden computations

INSTALLATION

pip install myeda

QUICK START

import myeda
import pandas as pd

df = pd.read_csv("data.csv")

myeda.dataset_overview(df)
myeda.missing_summary(df)
myeda.numeric_summary(df)
myeda.categorical_summary(df)

ONE-LINE EDA (ORCHESTRATOR)

from myeda import EDAReport

report = EDAReport(df)
results = report.run()

This returns:

Dataset overview

Missing value analysis

Numeric statistics

Categorical statistics

OPTIONAL VISUALIZATIONS

Visualizations are explicit and optional.

from myeda import (
plot_numeric_distribution,
plot_boxplot,
plot_categorical_counts,
plot_correlation_heatmap
)

plot_numeric_distribution(df, "Age")
plot_boxplot(df, "Fare")
plot_categorical_counts(df, "Sex")
plot_correlation_heatmap(df)

PROJECT STRUCTURE

EDA/
│
├── examples/
│   ├── titanic_dataset.csv
│   └── titanic_demo.ipynb
│
├── myeda/
│   ├── __init__.py
│   ├── report.py
│   │
│   ├── core/
│   │   ├── overview.py
│   │   ├── missing.py
│   │   └── statistics.py
│   │
│   └── viz/
│       └── visualization.py
│
├── tests/
│   └── test_statistics.py
│
├── setup.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


MODULE RESPONSIBILITIES

overview.py

Dataset shape

Column counts by type

Memory usage

Duplicate rows

missing.py

Missing value counts

Missing percentages

statistics.py

Numeric summaries

Categorical summaries

visualization.py

Histograms

Boxplots

Category counts

Correlation heatmaps

report.py

Orchestrates all EDA components

Provides one-line EDA execution

DEPENDENCIES

pandas

matplotlib

No seaborn
No plotly
No Jupyter-only features

TESTING

Tests are written using pytest.

python -m pytest

LICENSE

MIT License

ROADMAP

CLI support

JSON export of summaries

Target-based EDA helpers

Optional report export

AUTHOR

Khaja Mubashir Arsalan

NOTE

This library is intentionally simple and explicit.

If you need automated dashboards, use heavier tools.
If you want speed, clarity, and control, myeda is designed for you.