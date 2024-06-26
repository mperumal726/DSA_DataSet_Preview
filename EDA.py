import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
import streamlit.components.v1 as stc
# 

st.set_page_config(page_title='EDA_DataSets',page_icon='🕸️')
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Exploratory Data Analysis </h1>
        <h4 style="color:white;text-align:center;"> (Common info about the dataset) </h4>
		</div>
		"""
def main():
        
    
    # with st.container(border=True):
        with st.sidebar:
            st.html(html_temp)
            uploaded_file=st.file_uploader('Please Upload The(.csv,OR .xlsx) File: ')

        with st.container(border=True):
                        
            if uploaded_file is not None:
                df=pd.read_csv(uploaded_file)
                st.success('File Successfully Uploaded')

                # with st.expander('Preview Dataset'):
                #     st.dataframe(df)
                if uploaded_file is not None:
                    st.header('Preview Dataset')
                    if st.button('1.Head'):
                        st.dataframe(df.head())
                    if st.button('2.Tail'):
                        st.dataframe(df.tail())


                with st.expander('3.Check Datatype of Each Column'):
                    st.dataframe(df.dtypes)
                with st.expander('4.Check columns information '):
                    colum=df.columns
                    st.write(colum)
                        
                    
                with st.expander('5.Get Overall Statistics.'):

                    cradi=st.radio('Choose Include type ()',('All','Object','int'))
                    if cradi=='All':
                        st.dataframe(df.describe(include='all'))
                    elif cradi =='Object':
                        st.dataframe(df.describe(include=[object]))
                    elif cradi == 'int':
                        st.dataframe(df.describe())
                    
                with st.expander('6.Check Data Dimension .'): 
                    st.write('Data Dimension ',df.ndim) 


                with st.expander('7.Find Shape and Size Of Our DataSet'):
                    shap=st.radio('',('Row','Columns','Total Size'))
                    if shap=='Row':
                        st.write('Row',df.shape[0])
                    elif shap =='Columns':
                        st.write('Columns',df.shape[1])
                    else:
                        st.write('Total Size of the DataSet',df.size)
                    
                with st.expander('8.Find the DataSet Value_count'):
                    col=df.columns
                        
                    fear=st.selectbox('Select the columns',col)
                        
                    val=st.radio('To view in ',('Number','Percentage'))
                    if val=='Number':
                        st.write(df[fear].value_counts(normalize=False))
                    elif val=='Percentage':
                        st.write(df[fear].value_counts(normalize=True )*100)
                with st.expander('9.Find Null Values in The Dataset :'):
                    for col in df:
                        st.write(col ,'Column As',df[col].notna().sum(),'Value And',df[col].isna().sum(),'Missing Vaues')
                with st.expander('10.Check GroupBy Columns '):
                    cl=df.columns
                    fs=st.selectbox('Select the colum',cl)
                    gr=st.multiselect('select the groupby columns',cl)
                    st.write(df.groupby([fs])[gr].count())

                with st.expander('11.To Display Unique/Nunique Value from Each colums of the DataSet'):
                   
                    un=st.selectbox('To Choose: ',('Unique','Nunique'))
                    cl2=df.columns
                    if un=='Unique':
                        sel1=st.radio('Select the columns',cl2)
                        st.write(sel1,df[sel1].unique())

                    elif un=='Nunique':
                        sel=st.radio('Select the columns',cl2)
                        st.write('\n',sel,'\t',df[sel].nunique())

                with st.expander('12.Find Duplicate Values in the dataset'):
                    a=df.columns
                    test=df[a].duplicated().any()
                    
                    if test==True:
                        st.warning('This DataSet Containes Some Duplicate Value ')
                        dup=st.radio('Do you want to remove Duplicate Value',('Yes','No'))
                        if dup=='Yes':
                            df=df.drop_duplicates()
                            st.success('Removed Duplicate value')
                        elif dup=='No':
                            st.write('No problem Thanks ')
                    else:
                        st.success('No Duplicate Value in the Dataset')
                with st.expander('Do you want to Download File '):
                    if st.button('Yes'):
                        open('Data_csv','w').write(df.to_csv())
                        st.success('Successfully Saved File ')
                    if st.button('No'):
                        st.info('OK,Thanks')


        with st.sidebar: 
            
            # if st.checkbox("By"):
            st.success('Muruga Perumal Iyadurai',icon= '👉')  
            st.link_button('Linkedin','https://www.linkedin.com/in/muruga-perumal-iyadurai-7693592a7/')
                
            # if st.checkbox("About_App"):
            #     with st.container(border=True):
            #         st.markdown(''' 
            #                     ## Streamlit is an open-source Python library 
            #                     that makes it easy to create and share beautiful,custom web apps for machine learning and data science. 
            #                     In just a few minutes you can build and deploy powerful data apps
            #                     ''')
                    # st.balloons ()
            
          
            


                    

if __name__ == '__main__':
    main()

        

