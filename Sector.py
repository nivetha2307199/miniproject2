import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
def sec():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('select s.Ticker,c.sector,s.Close,s.Month from stockdataset s JOIN sector_data c on S.Ticker=c.COMPANY ')
    myresult=mycursor.fetchall()
    df1=pd.DataFrame(myresult,columns=["Company","Sector","Close","Month"])
    sector=st.sidebar.multiselect(label="Filter Sector",options=df1['Sector'].unique())
    if sector:
        df = df1[df1['Sector'].isin(sector)]
        first_close = df.groupby('Sector').first()['Close']
        last_close = df.groupby('Sector').last()['Close']
        yearly_return = ((last_close - first_close) / first_close) * 100
        dic={'Sector':sector,'Yearlyreturn':yearly_return}
        new_df=pd.DataFrame(dic)
        fig = px.bar(new_df, x='Sector', y='Yearlyreturn', color='Sector', title="Stock Prices by Sector")
        st.plotly_chart(fig)
        st.title("Stock-wise Performance")
        st.subheader("Detailed Data view")
        st.dataframe(new_df)
    else:
        st.info("Please select one or more months from the sidebar.")
sec()