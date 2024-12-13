import pandas as pd # import pandas library

from constants import PATH # path & others constants definition

# Data sets names
cash_requests_path = 'extract - cash request - data analyst.csv'
fees_path = 'extract - fees - data analyst - .csv'
lexique_path = 'Lexique - Data Analyst.xlsx'

# Cargar datasets
cash_requests_df = pd.read_csv(f"{PATH}{cash_requests_path}")
fees_df = pd.read_csv(f"{PATH}{fees_path}")
lexique_df = pd.read_excel(f"{PATH}{lexique_path}", sheet_name=None)  # Load Excel Workbook, DATA DICTIONARY

# Preview the datasets structure and data
print("Cash Requests Dataset:")
print(cash_requests_df.head())

print("\nFees Dataset:")
print(fees_df.head())

print("\nLexique (Hojas disponibles):")
print(lexique_df.keys())

# Merge to relate the Datasets
# Strategy: Maintain all records for cohort analysis
# check the relation between fees->cash_request_id = cash_requests->id
fees_with_cash_requests = fees_df.merge(cash_requests_df[['id', 'created_at', 'amount']], left_on='cash_request_id', right_on='id', how='left')

# Identify the nulls and duplicates values
missing_cash_requests = fees_with_cash_requests['id_y'].isnull().sum()
duplicates_in_fees = fees_df['cash_request_id'].duplicated().sum()

# Relation Summary between Datasets
relationship_summary = {
    "Total fees records": len(fees_df),
    "Total cash requests records": len(cash_requests_df),
    "Matched fees with cash requests": len(fees_with_cash_requests) - missing_cash_requests,
    "Unmatched fees (missing cash requests)": missing_cash_requests,
    "Duplicate cash_request_id in fees": duplicates_in_fees,
}

# Display the summary results
print("\nRELATIONS AND DATA PROBLEMS SUMMARY:")
for key, value in relationship_summary.items():
    print(f"  {key}: {value}")