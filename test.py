import streamlit as st
import pandas as pd
import plotly.express as px

# Layout
c1, c2, c3 = st.columns(3)
with c2:
    st.header("Bar Chart with Filter Options")

# File uploader
upload = st.file_uploader('Upload File', type=["csv"])

if upload is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(upload)

    # Display the first few rows of the dataframe
    st.write(df.head())

    # Numeric column statistics
    if 'Pclass' in df.columns:
        counting = df['Pclass'].count()
        summation = df['Pclass'].sum()
    else:
        counting = 0
        summation = 0
    
    # Columns for selecting plot parameters
    col1, col2, col3 = st.columns(3)
    
    # Get columns for x and y axes
    numeric_cols = df.columns.to_list()
    
    with col1:
        y = st.selectbox("Y Axis Label", numeric_cols)
    
    with col2:
        x = st.selectbox("X Axis Label", numeric_cols)
    
    with col3:
        # Add options to filter by sum or count of the Salary column
        filter_option = st.selectbox("Filter by", ["None", "Count of Salary", "Sum of Salary"])
    
    # Generate the bar chart
    if x in df.columns and y in df.columns:
        if filter_option == "Count of Pclass":
            # Create a DataFrame with count of Salary
            filtered_df = df.groupby(x)['Pclass'].count()
            bar = px.bar(filtered_df, x=filtered_df.index , y=filtered_df.values, title="Bar Chart with Count of Salary")
        
        elif filter_option == "Sum of Pclass":
            # Create a DataFrame with sum of Salary
            filtered_df = df.groupby(x)['Pclass'].sum().reset_index(name='Sum of Salary')
            bar = px.bar(filtered_df, x=filtered_df.index, y=filtered_df.values, title="Bar Chart with Sum of Salary")
        
        else:
            # Regular bar chart without filtering
            bar = px.bar(df, x=x, y=y, title="Bar Chart without Filtering")

        st.plotly_chart(bar)
    else:
        st.write("Please select valid columns for x and y axes.")