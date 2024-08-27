import streamlit as st 
import pandas as pd 
import numpy as np
import seaborn as sns
import datetime as dt 
df=pd.read_excel(r'E:\data analysis\projects part 2\v1.xlsx',sheet_name='InputData')
df['SALE TYPE'].value_counts() # three category
df['PAYMENT MODE'].value_counts() #two category
df.drop(columns=['DISCOUNT %','PRODUCT ID','MasterData.UOM','concat','day'],
        axis=1,inplace=True)
df['month']=df['DATE'].dt.month_name()
df.isnull().sum()
df.dropna(inplace=True)
# df[df.duplicated()]
# df.shape
df.info()
df.select_dtypes(np.number).describe()

q1=df.groupby('year')['total selling'].sum().reset_index(name='value')
q2=df.groupby('SALE TYPE')['total selling'].sum().reset_index(name='value')
q3=df.groupby('PAYMENT MODE')['total selling'].sum().reset_index(name='value')

q4=df.groupby('year')['total buing values'].sum().reset_index(name='value')
q5=df.groupby('SALE TYPE')['total buing values'].sum().reset_index(name='value')
q6=df.groupby('PAYMENT MODE')['total buing values'].sum().reset_index(name='value')

q7=df['SALE TYPE'].value_counts()
q8=df['PAYMENT MODE'].value_counts()



q11=df.groupby('PRODUCT')['total selling'].sum().sort_values(ascending=False).head(10)

# q11=df.groupby('PRODUCT')['total selling'].sum().sort_values(ascending=False).head(10)

st.markdown(
    """
    <h1 style='text-align: center;color:#E9967A'>first project</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stSlider > div > div > div > div {
        background-color: #ff6347;
        font-color:#E9967A
    }
    </style>
    """,
    unsafe_allow_html=True
)
length=st.slider("Choose the Number of Row that Should Showing ",min_value=5,
                max_value=len(df),step=1)
columns=st.multiselect("Select The Columns",df.columns.to_list()
                        ,default=df.columns.to_list(
                        
                        ))
st.write(df[:length][columns])


st.markdown(
    """
    <h1 style='text-align: center;color:#E9967A'>You Can Select The Filter blew </h1>
    <br>  <!-- This adds an empty line -->
    <br>  <!-- This adds an empty line -->
    <br>  <!-- This adds an empty line -->
    """,
    unsafe_allow_html=True
)

s1,s2,s3,s4=st.columns(4)
with s1:
    se=st.selectbox("CHOOSE PAYMENT MODE",[i for i in df['PAYMENT MODE'].unique()])
with s2:
    see=st.selectbox("SALE TYPE",[i for i in df['SALE TYPE'].unique()])
with s3:
    se1=st.selectbox("DATE",[i for i in df['year'].unique()])
with s4:
    se5=st.selectbox("DATE",[i for i in df['month'].unique()])
q9=df[(df['PAYMENT MODE']==se)&(df['SALE TYPE']==see)&(df['year']==se1)&(df['month']==se5)]['total selling'].sum().round(4)
q10=df[(df['PAYMENT MODE']==se)&(df['SALE TYPE']==see)&(df['year']==se1)&(df['month']==se5)]['total buing values'].sum().round(4)
q20=df[(df['PAYMENT MODE']==se)&(df['SALE TYPE']==see)&(df['year']==se1)&(df['month']==se5)]['SELLING PRICE'].sum().round(4)
q21=df[(df['PAYMENT MODE']==se)&(df['SALE TYPE']==see)&(df['year']==se1)&(df['month']==se5)]['BUYING PRIZE'].sum().round(4)

col1,col2=st.columns(2)
with col1:
           st.markdown(
        f"""
        <div style='font-size:20px; color:#E9967A; font-family:Arial;'>
            TOTAL SELLING AMOUNT: {q9}
        </div>
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        """,
        unsafe_allow_html=True
    )
with col2:
      st.markdown(
        f"""
        <div style='font-size:20px; color:#E9967A; font-family:Arial;'>
            TOTAL BUYING AMOUNT: {q10}
        </div>
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        
        """,
        unsafe_allow_html=True
    )
col1,col2=st.columns(2)
with col1:
           st.markdown(
        f"""
        <div style='font-size:20px; color:#E9967A; font-family:Arial;'>
            SELLING PRICE IS: {q20}
        </div>
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        """,
        unsafe_allow_html=True
    )
with col2:
      st.markdown(
        f"""
        <div style='font-size:20px; color:#E9967A; font-family:Arial;'>
            BUYING PRIZE IS: {q21}
        </div>
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        <br>  <!-- This adds an empty line -->
        """,
        unsafe_allow_html=True
    )


# date_range = st.slider(
#     "Select Date Range",
#     min_value=df['DATE'].min(),
#     max_value=df['DATE'].max(),
#     value=(df['DATE'].min(), df['DATE'].max())
# )
import plotly.express as px 
s1,s2=st.columns(2)
with s1:
    se=st.selectbox("COLUMN IN X AXIS",[i for i in df.select_dtypes('object')])
with s2:
    see=st.selectbox("COLUMN IN Y AXIS",[i for i in df.select_dtypes(np.number)])


q1=df.groupby(se)[see].sum()
bar1=px.bar(x=q1.index,y=q1.values, text_auto=True,
                labels={
        "x":se,
        "y":see
    })
st.plotly_chart(bar1)


st.markdown(
    """
    <h1 style='text-align: center;color:#E9967A'>You Can Select The Filter To Make Pie Chart </h1>
    <br>  <!-- This adds an empty line -->
    <br>  <!-- This adds an empty line -->
    <br>  <!-- This adds an empty line -->
    """,
    unsafe_allow_html=True
)
col1,col2,col3=st.columns(3)
with col1:
    e1=st.selectbox("CHOOSE THE COLUMN FOR VALUES ",
                    ['BUYING PRIZE','SELLING PRICE',
                     'total buing values','total selling'])
with col3:
    e=st.selectbox("CHOOSE THE COLUMN",['SALE TYPE','PAYMENT MODE'])
q7=df.groupby(e)[e1].sum().reset_index()
fig = px.pie(q7, names=e, values=e1,
                color=e1,  # Dynamically color based on values
                color_discrete_sequence=px.colors.sequential.Viridis   
             )
st.plotly_chart(fig)

col1,col2,col3=st.columns(3)
with col1:
    e1=st.selectbox("CHOOSE THE X AXIS",
                    [i for i in df.select_dtypes(np.number).drop('year',axis=1)])
with col3:
    e=st.selectbox("CHOOSE THE Y AXIS",[i for i in df.select_dtypes(np.number).drop('year',axis=1)])

fig = px.scatter(
    df, 
    x=e1,  # Column for x-axis
    y=e,  # Column for y-axis
    size=e,  # Size of points based on this column
    title=f"Scatter Plot for {e1} and {e}",  # Title of the plot
    labels={"X":e1, "Y":e}  # Custom axis labels
)
st.plotly_chart(fig)












