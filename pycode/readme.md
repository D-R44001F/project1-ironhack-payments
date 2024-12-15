# Python Code for Data Analysis Project

## Overview

This folder contains the Python scripts that implement the core processes of the **Data Analysis Project** hosted in the repository [project1-ironhack-payments](https://github.com/D-R44001F/project1-ironhack-payments). These scripts focus on automating and executing:

- **ETL (Extract, Transform, Load):** Efficiently processing raw data and preparing it for analysis.
- **EDA (Exploratory Data Analysis):** Analyzing data for patterns, trends, and quality issues.
- **Visualization:** Creating data visualizations to communicate findings effectively.

These scripts are designed for production and operational use, complementing the detailed, exploratory work presented in the [notebooks](https://github.com/D-R44001F/project1-ironhack-payments/tree/main/notebooks) folder.

---

## Scripts Included

### 1. **ETL Process**

- **Script:** `01-exploratory.py`
- **Description:**
  - Automates the extraction of raw data from source files.
  - Performs data transformations, such as cleaning, formatting, and normalization.
  - Loads the processed data into structured formats for further analysis.

### 2. **Exploratory Data Analysis (EDA)**

- **Script:** `02-data-cleaning.py`
- **Description:**
  - Implements descriptive statistics and summary visualizations.
  - Identifies data distributions, correlations, and anomalies.
  - Generates key insights for further exploration or reporting.

### 3. **Data Visualization**

- **Script:** `03-descriptvie-statistics-visualization.py`
- **Description:**
  - Automates the creation of visualizations, including bar charts, scatter plots, and histograms.
  - Exports visualizations in various formats for reporting and presentation.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/D-R44001F/project1-ironhack-payments.git
   ```
2. Navigate to the `pycode` folder:
   ```bash
   cd project1-ironhack-payments/pycode
   ```
3. Run the desired script:
   - For ETL:
     ```bash
     python 01-exploratory.py
     ```
   - For EDA:
     ```bash
     python 02-data-cleaning.py
     ```
   - For Visualization:
     ```bash
     python 03-descriptvie-statistics-visualization.py
     ```
     ```bash
     python FrequencyServicesUsagge.py
     ```

---

## Relation to Jupyter Notebooks

While the scripts in this folder are optimized for operational use, the [notebooks folder](https://github.com/D-R44001F/project1-ironhack-payments/tree/main/notebooks):

- Provides detailed step-by-step explanations for each process.
- Focuses on the educational and exploratory aspects of the project.
- Serves as a complementary resource for understanding the logic implemented in these scripts.

---

## Contact

For questions or further details, please contact the project team via the repository's Issues or Discussions section.
