import pandas as pd
import matplotlib.pyplot as plt

#Load dataset
df = pd.read_csv('project_dataset/consolidated_ironhack_data.csv')
df.head()

#1. Metric to analyze: Frequncy of Service Usage
# Filter for "instant" type transactions
cash_advance_df = df[df["type"] == "instant_payment"]

# Count the total number of transactions per cohort (group by 'cohort_month')
cohort_transaction_count = cash_advance_df.groupby('cohort_month')['fee_id'].count().reset_index(name='total_transactions')

# Count the number of unique users per cohort
cohort_user_count = cash_advance_df.groupby('cohort_month')['cash_request_id'].nunique().reset_index(name='total_users')

# Calculate the average transactions per user in each cohort
cohort_frequency = cohort_transaction_count.merge(cohort_user_count, on='cohort_month')
cohort_frequency['average_transactions_per_user'] = cohort_frequency['total_users']

# Merge cohort information back into the main dataframe
df = df.merge(first_cash_advance[['cohort_month']], on='cash_request_id', how='left')

# Plot the frequency of cash advance usage by cohort month
plt.figure(figsize=(10, 6))
plt.plot(cohort_frequency['cohort_month'].astype(str), cohort_frequency['average_transactions_per_user'], marker='o')
plt.title("Frequency of Service Usage of Cash Advance by Cohort")
plt.xlabel("Cohort Month")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()