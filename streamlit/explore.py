import streamlit as st
import pandas as pd

from constants import PATH # path & others constants definition

def app():
    # Titles and Introduction
    st.title("Cohort Data Analysis")
    st.markdown("This interactive dashboard allows you to load and analyze datasets for cohort analysis and dataset relationships.")
    
    # Dataset paths
    cash_requests_path = 'extract - cash request - data analyst.csv'
    fees_path = 'extract - fees - data analyst - .csv'
    lexique_path = 'Lexique - Data Analyst.xlsx'
    
    # Load datasets with Streamlit
    st.header("Dataset Loading")
    st.markdown("**Automatic loading of the datasets below:")
    try:
        # Load datasets
        cash_requests_df = pd.read_csv(f"{PATH}{cash_requests_path}")
        fees_df = pd.read_csv(f"{PATH}{fees_path}")
        lexique_df = pd.read_excel(f"{PATH}{lexique_path}", sheet_name=None)
    
        st.success("Datasets successfully loaded.")
    except Exception as e:
        st.error(f"Error loading datasets: {e}")
        st.stop()
    
    # Preview datasets
    st.header("Dataset Preview")
    if st.checkbox("Show Cash Requests Dataset"):
        st.dataframe(cash_requests_df.head())
    
    if st.checkbox("Show Fees Dataset"):
        st.dataframe(fees_df.head())
    
    if st.checkbox("Show Lexique (Available Sheets)"):
        st.write("Available sheets:", list(lexique_df.keys()))
    
    # Merge datasets
    st.header("Dataset Relationship Analysis")
    fees_with_cash_requests = fees_df.merge(
        cash_requests_df[['id', 'created_at', 'amount']], 
        left_on='cash_request_id', 
        right_on='id', 
        how='left'
    )
    
    # Identify nulls and duplicates
    missing_cash_requests = fees_with_cash_requests['id_y'].isnull().sum()
    duplicates_in_fees = fees_df['cash_request_id'].duplicated().sum()
    
    # Relationship summary
    relationship_summary = {
        "Total Fees Records": len(fees_df),
        "Total Cash Requests Records": len(cash_requests_df),
        "Fees Matched with Cash Requests": len(fees_with_cash_requests) - missing_cash_requests,
        "Unmatched Fees (Missing Cash Requests)": missing_cash_requests,
        "Duplicate cash_request_id in Fees": duplicates_in_fees,
    }
    
    st.subheader("Relationship and Data Issues Summary")
    st.json(relationship_summary)
    
    # Interactive exploratory analysis
    st.header("Interactive Exploratory Analysis")
    st.markdown("Use the tools below to further explore the data.")
    
    data_to_explore = st.selectbox(
        "Select the dataset to explore:",
        ["Cash Requests", "Fees", "Fees with Cash Requests"]
    )
    
    if data_to_explore == "Cash Requests":
        st.dataframe(cash_requests_df)
    elif data_to_explore == "Fees":
        st.dataframe(fees_df)
    else:
        st.dataframe(fees_with_cash_requests)
    
    # Interactive charts
    st.header("Data Visualizations")
    st.markdown("Generate quick visualizations for the loaded datasets.")
    
    if st.checkbox("Show distribution of amounts in Cash Requests"):
        st.bar_chart(cash_requests_df['amount'].value_counts())
    
    if st.checkbox("Show Fees by status"):
        if 'status' in fees_df.columns:
            st.bar_chart(fees_df['status'].value_counts())
        else:
            st.warning("The 'status' column is not available in the Fees Dataset.")
    
    # Conclusion
    st.header("Conclusion")
    st.markdown("This interactive analysis allows identifying relationships between datasets, data quality issues, and provides visualizations for deeper insights.")
