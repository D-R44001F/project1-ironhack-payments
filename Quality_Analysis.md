# Project 1 - IronHack Payments

## Data Quality Analysis

Now that the relevant data fields have been found and sorted, we need to validated the quality of the data to ensure accuracy on the results. We star this by checking for empty values or missing
data.

To achieve this, we use the following code on the consolidated data:
```python
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
```

Output:
Missing Values in Each Column:
| Column                   | Missing Values |
|--------------------------|----------------|
| fee_id                   | 0              |
| cash_request_id          | 0              |
| type                     | 0              |
| status                   | 0              |
| category                 | 18,861         |
| total_amount             | 0              |
| reason                   | 0              |
| fee_created_at           | 0              |
| updated_at               | 0              |
| paid_at                  | 5,526          |
| from_date                | 13,291         |
| to_date                  | 13,291         |
| charge_moment            | 0              |
| cash_request_id.1        | 0              |
| cash_request_created_at  | 0              |
| cash_request_amount      | 0              |


Number of Columns with Missing Values: 4
All Columns Have Missing Values: False
Total Missing Values in the DataFrame: 50969
