import streamlit as st 
import pandas as pd 
import numpy as np
# import seaborn as sns
c1,c2,c3=st.columns(3)
with c2:
    st.header("first project")
import plotly.express as px 
upload=st.file_uploader('Upload File',type=["csv"])

if upload is not None:
    df=pd.read_csv(upload)
    length=st.slider("Choose the Number of Row that Should Showing ",min_value=5,
                     max_value=len(df),step=1)
    columns=st.multiselect("Select The Columns",df.columns.to_list()
                           ,default=df.columns.to_list(
                               
                           ))
    st.write(df[:length][columns])
    counting=df['Pclass'].count()
    sumtion=df['Pclass'].sum()
    col1,col2,col3,col4=st.columns(4)
    col=df.select_dtypes(np.number).columns.to_list()
    hue=df.columns.to_list()
    with col1:
        y=st.selectbox("Y axis Label ",col)
    with col2:    
        x=st.selectbox("X axis Label ",col)
    with col3:    
        color=st.selectbox("Color Label ",df.columns)
    with col4:    
        sum=st.selectbox("Color Label ",[counting,sumtion]) 
    tab1,tab2=st.tabs(2)  
    with tab1:     
        scatter=px.scatter(df,x=x,y=y,color=color)
        st.plotly_chart(scatter)
    with  tab2:     
        bar=px.bar(df,x=x,y=y,color=color)
        st.plotly_chart(bar)

# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# # Layout
# c1, c2, c3 = st.columns(3)
# with c2:
#     st.header("First Project")

# # File uploader
# upload = st.file_uploader('Upload File', type=["csv"])

# if upload is not None:
#     # Read the uploaded CSV file
#     df = pd.read_csv(upload)
    
#     # Slider for selecting number of rows to display
#     length = st.slider("Choose the Number of Rows to Show", min_value=5, max_value=len(df), step=1)
    
#     # Multi-select for selecting columns to display
#     columns = st.multiselect("Select The Columns", df.columns.to_list(), default=df.columns.to_list())
    
#     # Display the selected rows and columns
#     st.write(df[columns].head(length))
    
#     # Numeric column statistics
#     if 'Pclass' in df.columns:
#         counting = df['Pclass'].count()
#         summation = df['Pclass'].sum()
#     else:
#         counting = 0
#         summation = 0
    
#     # Columns for selecting plot parameters
#     col1, col2, col3, col4 = st.columns(4)
    
#     # Get numeric columns for plotting
#     numeric_cols = df.columns.to_list()
    
#     with col1:
#         y = st.selectbox("Y Axis Label", numeric_cols)
    
#     with col2:
#         x = st.selectbox("X Axis Label", numeric_cols)
    
#     with col3:
#         color = st.selectbox("Color Label", df.columns.to_list() + ["Count of Pclass", "Sum of Pclass"])
    
#     with col4:
#         # Use a placeholder since 'sum' is a reserved keyword
#         color_option = st.selectbox("Choose Color Option", ["None", "Count of Pclass", "Sum of Pclass"])
    
#     # Tabs for different charts
#     tab1, tab2 = st.tabs(["Scatter Plot", "Bar Chart"])
    
#     with tab1:
#         if x in df.columns and y in df.columns:
#             # Handle color option for scatter plot
#             scatter = px.scatter(df, x=x, y=y, color=df[color] if color in df.columns else None)
#             st.plotly_chart(scatter)
#         else:
#             st.write("Please select valid columns for x and y axes.")
    
#     with tab2:
#         if x in df.columns and y in df.columns:
#             # Handle color option for bar chart
#             if color_option == "Count of Pclass":
#                 df['Count_of_Pclass'] = df['Pclass'].notna().astype(int)  # Create a count column
#                 bar = px.bar(df, x=x, y=y, color='Count_of_Pclass')
#             elif color_option == "Sum of Pclass":
#                 df['Sum_of_Pclass'] = summation  # Add the sum value
#                 bar = px.bar(df, x=x, y=y, color='Sum_of_Pclass')
#             else:
#                 bar = px.bar(df, x=x, y=y, color=None)
            
#             st.plotly_chart(bar)
#         else:
#             st.write("Please select valid columns for x and y axes.")








