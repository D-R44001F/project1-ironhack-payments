import pandas as pd # import pandas library

from constants import PATH # path & others constants definition

# Data sets names
consolidated = 'consolidated_ironhack_data.csv'

# Load datasets
consolidated_df = pd.read_csv(f"{PATH}{consolidated}")

# Select rows by Group ['category','cash_request_id']
groupby_df = (
    consolidated_df.groupby(['category', 'cash_request_id'], as_index=False)
    .agg({
        'cohort_month': 'first',  # Select first cohort_month
        'cash_request_id': 'first',  # Select first cash_request_id        
        'status': (lambda x: if x)'first',  # Select first status
        'cash_request_amount': 'sum'  # Sum cash_request_amount
    })
    .drop(columns=['category']) # Drop teh 'category' column
)

print(groupby_df)

# Save the new data set
groupby_file_path = f'{PATH}groupby_ironhack_data_1.csv'
groupby_df.to_csv(groupby_file_path, index=False)

print(f"\nGroup by ['category', 'cash_request_id'] dataset saved to: {groupby_file_path}")