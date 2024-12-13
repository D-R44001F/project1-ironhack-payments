import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data into pands series
data = pd.read_csv("./project_dataset/consolidated_ironhack_data.csv")

# Metadata
data_info = data.info()

# Check for missing values in the DataFrame
missing_values = pd.isnull(data)

# Count missing values in each column
missing_counts = missing_values.sum()

# Count columns with missing values
columns_with_missing = missing_counts[missing_counts > 0].count()

# Check if all columns have missing values
all_columns_missing = missing_counts.all()

# Calculate the total number of missing values
total_missing_values = missing_counts.sum()

# Display the results
print("Missing Values in Each Column:\n", missing_counts)
print("\nNumber of Columns with Missing Values:", columns_with_missing)
print("All Columns Have Missing Values:", all_columns_missing)
print("\nTotal Missing Values in the DataFrame:", total_missing_values)

# Finding incidents
unique_values = data['type'].unique()
unique_count = data['type'].value_counts()

print(unique_values, unique_count)

# Show the count of 'types' 
unique_count.plot(kind="bar", title="Comparison")
plt.xticks(rotation=0)
plt.ylabel("Ocurrences")
plt.show()

# Incident Rate by Month
cohort_counts = data['cohort_month'].value_counts().sort_index()
# Display Incident Rate Analysis
print("\nDisplay Incident Rate Analysis")
# Filter dataset for incidents
incident_data = data[data['type'] == 'incident']
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

# Incident by Month
# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(incident_counts_by_cohort.index, incident_counts_by_cohort.values, color='skyblue')

# Titles and labels
plt.title('Incident Counts by Cohort', fontsize=16)
plt.xlabel('Cohort Month', fontsize=12)
plt.ylabel('Incident Count', fontsize=12)
plt.xticks(rotation=45, fontsize=10)  # Rotate labels for better readability

# Show the plot
plt.tight_layout()
plt.show()

