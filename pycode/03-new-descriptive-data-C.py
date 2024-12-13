import pandas as pd
import matplotlib.pyplot as plt

from constants import PATH # path & others constants definition

#Load dataset
df = pd.read_csv(f'{PATH}consolidated_ironhack_data.csv')
print(df.head())

#1. Metric to analyze: Frequncy of Service Usage
# Filter for "instant" type transactions
cash_advance_df = df[df["type"] == "instant_payment"]

# Count the total number of transactions per cohort (group by 'cohort_month')
cohort_transaction_count = cash_advance_df.groupby('cohort_month')['fee_id'].count().reset_index(name='total_transactions')
print(cohort_transaction_count)

# Plot the frequency of cash advance usage by cohort month
plt.figure(figsize=(10, 6))
plt.plot(cohort_transaction_count['cohort_month'].astype(str), cohort_transaction_count['total_transactions'], marker='o')
plt.title("Transactions by Cohort")
plt.xlabel("Cohort Month")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()