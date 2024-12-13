#!pip install pandas
import pandas as pd # import pandas library
#!pip install matplotlib.pyplot
import matplotlib.pyplot as plt #import pyplot library

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

# Exclude records with no values
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

# Descriptive Analysis and Empty Values
print("\nDescriptive Statistics:")
print(fees_cleaned.describe())

missing_values_summary = fees_cleaned.isnull().sum()
print("\nEmpty values on each column:")
print(missing_values_summary)

# Display amount distribution
print("\nDisplay amount distribution")
plt.hist(fees_cleaned['cash_request_amount'].dropna(), bins=50, edgecolor='k', alpha=0.7)
plt.title('Amount Request Distribution')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

# Consolidate datasets 
consolidated_df = fees_cleaned.copy()

# Create a new column 'cohort_month' based on the creation month in 'cash requests'
consolidated_df['cohort_month'] = pd.to_datetime(consolidated_df['cash_request_created_at']).dt.to_period('M')

# Display rows per cohorts
print("\nDisplay rows per cohorts")
cohort_counts = consolidated_df['cohort_month'].value_counts().sort_index()
plt.bar(cohort_counts.index.astype(str), cohort_counts.values, alpha=0.7)
plt.title('Rows per Cohorts')
plt.xlabel('Cohort (Month)')
plt.ylabel('Requests Count')
plt.xticks(rotation=45)
plt.show()

# Display Incident Rate Analysis
print("\nDisplay Incident Rate Analysis")
# Filter dataset for incidents
incident_data = consolidated_df[consolidated_df['type'] == 'incident']
incident_counts_by_cohort = incident_data['cohort_month'].value_counts().sort_index()
cohort_counts = cohort_counts.sort_index()  # Ensure both series are aligned
incident_rate_by_cohort = (incident_counts_by_cohort / cohort_counts).fillna(0)

plt.plot(incident_rate_by_cohort.index.astype(str), incident_rate_by_cohort.values, marker='o')
plt.title('Incident Rate per Cohort Month')
plt.xlabel('Cohort Month')
plt.ylabel('Incident Rate')
plt.xticks(rotation=45)
plt.grid(alpha=0.5)
plt.show()


