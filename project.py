import streamlit as st 


# col1,col2,col3=st.

st.header("first project")
side=st.sidebar.title("the side of the filter")
with side:
    select=st.selectbox("please select any option",["Circle","Rectangle"])

if  select=="Circle":
    redi=st.number_input("Redius",min_value=0,max_value=100,step=1)
    Area=redi * redi * 3.14
    Perimeter=2 * 3.14 * redi
    
if select =="Rectangle":
    height=st.number_input("Length",min_value=0,max_value=100,step=1)
    width=st.number_input("width",min_value=0,max_value=100,step=1)
    Area=width * height
    Perimeter=(width+height)*2


compute=st.button("compute Area and Perimeter")    

if compute:
    st.write("Area is :", Area)
    st.write("Perimeter is :", Perimeter)
    






















