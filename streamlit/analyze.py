import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from constants import PATH # path & others constants definition

def app():
    # Titles and Introduction
    st.title("Cohort Analysis and Incident Rate Dashboard")
    st.markdown("This interactive dashboard allows you to analyze cohorts, visualize data distributions, and explore incident rates.")
    
    cash_requests_path = 'extract - cash request - data analyst.csv'
    fees_path = 'extract - fees - data analyst - .csv'

    # Load datasets with Streamlit
    st.header("Dataset Loading")
    st.markdown("**Automatic loading of the datasets below:")
    try:
        # Load datasets
        cash_requests_df = pd.read_csv(f"{PATH}{cash_requests_path}")
        fees_df = pd.read_csv(f"{PATH}{fees_path}")
    
        st.success("Datasets successfully loaded.")
    except Exception as e:
        st.error(f"Error loading datasets: {e}")
        st.stop()
    
    # Merge datasets
    st.header("Data Cleaning and Merging")
    fees_with_cash_requests = fees_df.merge(
        cash_requests_df[['id', 'created_at', 'amount']], 
        left_on='cash_request_id', 
        right_on='id', 
        how='left'
    )
    
    fees_cleaned = fees_with_cash_requests[~fees_with_cash_requests['id_y'].isnull()].copy()
    st.write("Rows in fees after excluding non-matching:", len(fees_cleaned))
    
    # Rename columns
    fees_cleaned.rename(
        columns={
            'id_x': 'fee_id',
            # 'id_y': 'cash_request_id',
            'created_at_x': 'fee_created_at',
            'created_at_y': 'cash_request_created_at',
            'amount': 'cash_request_amount'
        }, inplace=True
    )
    st.write("Cleaned Dataset:")
    st.dataframe(fees_cleaned.head())
    
    # Descriptive Statistics
    st.header("Descriptive Statistics")
    st.write(fees_cleaned.describe())
    
    # Missing Values
    st.subheader("Missing Values Summary")
    missing_values_summary = fees_cleaned.isnull().sum()
    st.write(missing_values_summary)
    
    # Distribution of Amounts
    st.subheader("Amount Request Distribution")
    fig, ax = plt.subplots()
    ax.hist(fees_cleaned['cash_request_amount'].dropna(), bins=50, edgecolor='k', alpha=0.7)
    ax.set_title('Amount Request Distribution')
    ax.set_xlabel('Amount')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
    # Add cohort_month column
    fees_cleaned['cohort_month'] = pd.to_datetime(fees_cleaned['cash_request_created_at']).dt.to_period('M')
    consolidated_df = fees_cleaned.copy()
    
    # Rows per Cohort
    st.subheader("Rows per Cohort")
    cohort_counts = consolidated_df['cohort_month'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(cohort_counts.index.astype(str), cohort_counts.values, alpha=0.7)
    ax.set_title('Rows per Cohorts')
    ax.set_xlabel('Cohort (Month)')
    ax.set_ylabel('Requests Count')
    ax.set_xticklabels(cohort_counts.index.astype(str), rotation=45)
    st.pyplot(fig)
    
    # Incident Rate Analysis
    st.subheader("Incident Rate Analysis")
    if 'type' in consolidated_df.columns:
        incident_data = consolidated_df[consolidated_df['type'] == 'incident']
        incident_counts_by_cohort = incident_data['cohort_month'].value_counts().sort_index()
        cohort_counts = cohort_counts.sort_index()
        incident_rate_by_cohort = (incident_counts_by_cohort / cohort_counts).fillna(0)
    
        fig, ax = plt.subplots()
        ax.plot(incident_rate_by_cohort.index.astype(str), incident_rate_by_cohort.values, marker='o')
        ax.set_title('Incident Rate per Cohort Month')
        ax.set_xlabel('Cohort Month')
        ax.set_ylabel('Incident Rate')
        ax.grid(alpha=0.5)
        ax.set_xticklabels(incident_rate_by_cohort.index.astype(str), rotation=45)
        st.pyplot(fig)
    else:
        st.warning("Column 'type' is missing from the dataset.")
    
    
    
    # Stablish cohort_month as category
    consolidated_df['cohort_month'] = consolidated_df['cohort_month'].astype(str)
    
    # Count or Frequency
    cohort_counts = consolidated_df['cohort_month'].value_counts().sort_index()
    
    # Cerate the Graph
    fig, ax = plt.subplots(figsize=(10, 6))  
    ax.bar(cohort_counts.index, cohort_counts.values, color='skyblue', edgecolor='black', alpha=0.7)
    ax.set_title('Cohort Trends: Number of Requests per Cohort', fontsize=14)
    ax.set_xlabel('Cohort Month', fontsize=12)  
    ax.set_ylabel('Number of Requests', fontsize=12)  
    ax.set_xticks(range(len(cohort_counts.index)))  
    ax.set_xticklabels(cohort_counts.index, rotation=45, fontsize=10)  
    ax.tick_params(axis='y', labelsize=10)  
    plt.tight_layout()  
    
    # Display the Graph Streamlit
    st.pyplot(fig)
    
    # Conclusion
    st.header("Conclusion")
    st.markdown("This interactive dashboard provides insights into cohort-based data analysis, incident rates, and data distributions.")
    st.markdown("#### Results of the Exploratory Data Analysis (EDA)")
    st.markdown("**Descriptive Statistics:**")
    st.markdown("- The average request amount is $81.83 , ranging from $1 to $200.")
    st.markdown("- The average fee (total_amount) is constant at $5, except for outliers.")
    st.markdown("**Outliers:**")
    st.markdown("- Four records in the top 1% of request amounts are considered outliers.")
    st.markdown("**Distributions and Frequencies:**")
    st.markdown("- Most requests have amounts close to $50 and $100.")
    st.markdown("- Variations in the number of requests are observed across cohort months.")
    st.markdown("**Incident Rate:**")
    st.markdown("- The analysis revealed variable incident rates by month, indicating possible behavioral patterns.")
