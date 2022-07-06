import streamlit as st
def app(diabetes_df):
    st.write("""Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.

There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.

This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.""")
    with st.expander('View data'):
        st.dataframe(diabetes_df)
    st.subheader('Columns Description')
    col1,col2,col3=st.columns(3)
    with col1:
        if st.checkbox('Show all columns names',key=1):
            st.write(diabetes_df.columns)
    with col2:
        if st.checkbox('View column data-type',key=2):
            st.write(diabetes_df.describe())
    with col3:
        if st.checkbox('View column data',key=3):
            selected_column=st.selectbox('Select column',(diabetes_df.columns))
            st.write(diabetes_df[selected_column])