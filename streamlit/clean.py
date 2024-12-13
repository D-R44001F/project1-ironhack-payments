import streamlit as st
import pandas as pd

from constants import PATH # path & others constants definition

def app():
    # Titles and Introduction
    st.title("Cohort Data Cleaning and Consolidation")
    st.markdown("This interactive dashboard allows you to load, clean, and consolidate datasets for cohort analysis.")

    # Datasets Name
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
    st.header("Merge and Clean Datasets")
    fees_with_cash_requests = fees_df.merge(
        cash_requests_df[['id', 'created_at', 'amount']], 
        left_on='cash_request_id', 
        right_on='id', 
        how='left'
    )
    
    # Exclude records with null values
    fees_cleaned = fees_with_cash_requests[~fees_with_cash_requests['id_y'].isnull()].copy()
    st.write("Rows in fees after excluding non-matching:", len(fees_cleaned))
    
    # Rename columns
    fees_cleaned.rename(
        columns={
            'id_x': 'fee_id',
            # 'id_y': 'cash_request_id_y',
            'created_at_x': 'fee_created_at',
            'created_at_y': 'cash_request_created_at',
            'amount': 'cash_request_amount'
        }, inplace=True
    )
    st.write("Cleaned Fees Dataset:")
    st.dataframe(fees_cleaned.head())
    
    # Add cohort_month column
    fees_cleaned['cohort_month'] = pd.to_datetime(fees_cleaned['cash_request_created_at']).dt.to_period('M')
    st.write("Dataset with Cohort Month:")
    st.dataframe(fees_cleaned[['cohort_month', 'cash_request_amount']].head())
    
    # Consolidate datasets
    consolidated_df = fees_cleaned.copy()
    st.subheader("Consolidated Dataset")
    st.dataframe(consolidated_df.head())
    
    # Save consolidated dataset
    consolidated_file_path = f'{PATH}consolidated_ironhack_data.csv'
    try:
        consolidated_df.to_csv(consolidated_file_path, index=False)
        st.success(f"Consolidated dataset saved to: {consolidated_file_path}")
    except Exception as e:
        st.error(f"Error saving the consolidated dataset: {e}")
    
    # Columns Overview
    st.header("Columns Overview")
    st.markdown("### Fees with Cash Requests Columns:")
    st.write(list(fees_with_cash_requests.columns))
    st.markdown("### Cleaned Fees Columns:")
    st.write(list(fees_cleaned.columns))
    st.markdown("### Consolidated Columns:")
    st.write(list(consolidated_df.columns))
