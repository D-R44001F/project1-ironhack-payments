import pandas as pd # import pandas library

from constants import PATH # path & others constants definition

# Data sets names
cash_requests_path = 'extract - cash request - data analyst.csv'
fees_path = 'extract - fees - data analyst - .csv'

# Load datasets
cash_requests_df = pd.read_csv(f"{PATH}{cash_requests_path}")
fees_df = pd.read_csv(f"{PATH}{fees_path}")


# Merge to relate the Datasets
# check the relation between fees->cash_request_id = cash_requests->id
fees_with_cash_requests = fees_df.merge(cash_requests_df[['id', 'created_at', 'amount']], left_on='cash_request_id', right_on='id', how='left') 

# Exclude records with nulll values
fees_cleaned = fees_with_cash_requests[~fees_with_cash_requests['id_y'].isnull()].copy()

# Strategy: Maintain all records for cohort analysis
# After the data cleaning, Check the data integrity 
print("\nAfter first cleaning process:")
print(f"Rows in fees after excluding non-matching: {len(fees_cleaned)}")

# Rename columns 
fees_cleaned.rename(
   columns={
        'id_x': 'fee_id',
        'id_y': 'cash_request_id',
        'created_at_x': 'fee_created_at',
        'created_at_y': 'cash_request_created_at',
        'amount': 'cash_request_amount'  # Asegúrate de que 'amount' se renombre correctamente
    }, inplace=True
)
print(fees_cleaned)

# Create a new column 'cohort_month' based on the creation month in 'cash requests'
fees_cleaned['cohort_month'] = pd.to_datetime(fees_cleaned['cash_request_created_at']).dt.to_period('M')

# Consolidate datasets 
consolidated_df = fees_cleaned.copy()

# Confirm if the data has a time zone before applying the conversion
print(f'\nIs data has a time zone: {consolidated_df['cash_request_created_at'].dtype}')

# Display consolidated structure
print("\nConsolidated Dataset (head):")
print(consolidated_df.head())

# Display the columns on each df
print('\nFees with Cash Request\n',fees_with_cash_requests.columns)
print('\nFees Cleaned\n',fees_cleaned.columns)
print('\nConsolidate\n',consolidated_df.columns)

# Save the new data set
consolidated_file_path = f'{PATH}consolidated_ironhack_data.csv'
consolidated_df.to_csv(consolidated_file_path, index=False)

print(f"\nConsolidated dataset saved to: {consolidated_file_path}")