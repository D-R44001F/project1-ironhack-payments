# Datasets for Data Analysis Project

## Overview

This folder contains the datasets used for the data analysis project. The description or lexique for the data it is in **`Lexique - Data Analyst.xlsx`**. The most important dataset, **`consolidated_ironhack_data.csv`**, serves as the **single source of truth (SSOT)** for the study, analysis, and visualization of the data. It is the result of merging two other datasets:

- **`extract - cash request - data analyst.csv`**
- **`extract - fees - data analyst.csv`**

The merging process was performed using the relationship between the column `cash_request_id` in the **Fee dataset** and the column `id` in the **Cash Request dataset**. Each fee record corresponds to one or many rows in the Cash Request dataset.

---

## Description of Datasets

### 1. **`consolidated_ironhack_data.csv`** (Single Source of Truth - SSOT)

This dataset consolidates and enhances the other two datasets by verifying records and adding new columns to improve data examination and visualization. It includes:

- Verified rows.
- Enriched data with additional columns.
- Enhanced consistency for analysis and visualization purposes.

#### **Key Features**:

- **Total fee records:** 21,061
- **Matched fees with cash requests:** 21,057
- **Unmatched fees (missing cash requests):** 4
- **Duplicate `cash_request_id` in fees:** 8,127

- **Number of Columns with Missing Values:** 4
- **All Columns Have Missing Values: False**
- **Total Missing Values in the DataFrame:** 50969

#### **Missing Values Summary**:

| Column                  | Missing Values |
| ----------------------- | -------------- |
| fee_id                  | 0              |
| cash_request_id         | 0              |
| type                    | 0              |
| status                  | 0              |
| category                | 18,861         |
| total_amount            | 0              |
| reason                  | 0              |
| fee_created_at          | 0              |
| updated_at              | 0              |
| paid_at                 | 5,526          |
| from_date               | 13,291         |
| to_date                 | 13,291         |
| charge_moment           | 0              |
| cash_request_id.1       | 0              |
| cash_request_created_at | 0              |
| cash_request_amount     | 0              |

This dataset should be the primary resource for all analysis and visualization tasks.

---

### 2. **`extract - fees - data analyst.csv`**

This dataset contains information about fees generated in the system. Key columns include:

- **`id`**: Unique ID of the fee object.
- **`type`**: Type of fee. Possible values:
  - `instant_payment`: Fees for instant cash requests.
  - `split_payment`: Future fees for split payments.
  - `incident`: Fees for failed reimbursements.
  - `postpone`: Fees for postponed reimbursements.
- **`status`**: Status of the fee, such as `confirmed`, `rejected`, or `accepted`.
- **`category`**: Reason for the fee (e.g., `rejected_direct_debit`).
- **`total_amount`**: Total amount of the fee (including VAT).
- **`cash_request_id`**: Unique identifier linking the fee to a cash request.

---

### 3. **`extract - cash request - data analyst.csv`**

This dataset provides detailed information about cash requests. Key columns include:

- **`id`**: Unique ID of the cash request.
- **`status`**: Status of the cash request, such as `approved`, `rejected`, or `pending`.
- **`reason`**: Explanation for rejections (if applicable).
- **`created_at`**: Timestamp of cash request creation.
- **`cash_request_amount`**: Amount of the requested cash.
- **`reimbursement_date`**: Planned reimbursement date.

---

## Data Relationships and Integrity

- **Primary Relationship**: The datasets are joined using `cash_request_id` from the Fee dataset and `id` from the Cash Request dataset.
- **Key Insights**:
  - Each Fee record corresponds to one or multiple Cash Request records.
  - Data issues, such as missing or duplicate records, were identified and resolved during consolidation.

---

## How to Use

- **Dataset for Analysis**: Use `consolidated_ironhack_data.csv` for all analysis and visualization purposes.
- **Exploratory Analysis**: Leverage the dataset's enriched columns to perform exploratory data analysis (EDA).
- **Visualization**: Utilize this dataset to create dashboards or reports.
