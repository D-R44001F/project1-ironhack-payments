import pandas as pd
import matplotlib.pyplot as plt

from constants import PATH # path & others constants definition

# Load the consolidated dataset
consolidated_file_path = f'{PATH}consolidated_ironhack_data.csv'
consolidated_df = pd.read_csv(consolidated_file_path)

# Ensure 'cohort_month' is in string format for proper visualization
consolidated_df['cohort_month'] = consolidated_df['cohort_month'].astype(str)

# Count the number of requests per cohort month
cohort_counts = consolidated_df['cohort_month'].value_counts().sort_index()

# Create a bar chart for cohort trends
plt.figure(figsize=(10, 6))
plt.bar(cohort_counts.index, cohort_counts.values, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Cohort Trends: Number of Requests per Cohort', fontsize=14)
plt.xlabel('Cohort Month', fontsize=12)
plt.ylabel('Number of Requests', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()
