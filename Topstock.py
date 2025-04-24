import pandas as pd
import streamlit as st
import pymysql
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
def stock():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('Select * from stockdataset')
    myresult=mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=('S.no','Ticker','Close','Date','High','Low','Month','Open','Volume'))
    first_close = df.groupby('Ticker').first()['Close']
    last_close = df.groupby('Ticker').last()['Close']
    yearly_return = ((last_close - first_close) / first_close) * 100
    yearly_return = yearly_return.reset_index().rename(columns={'Close': 'Yearly Return'})
    returns_df = yearly_return.copy()
    top_green = returns_df.sort_values('Yearly Return', ascending=False,ignore_index=True).head(10)
    top_red = returns_df.sort_values('Yearly Return',ignore_index=True).head(10)
    col1,col2=st.columns(2)
    df1=pd.DataFrame(top_green,columns=['Ticker','Yearly Return'])
    df1=df1.head(10)
    df2=pd.DataFrame(top_red,columns=['Ticker','Yearly Return'])
    df2=df2.head(10)
    with col1:
        st.markdown("**Top 10 Green Stocks**")
        fig1, ax = plt.subplots()
        ax.plot(df1['Ticker'],df1['Yearly Return'], marker='o', linestyle='-', color='green', label='Yearly Return')
        ax.set_title("📍 Stock Returns with Markers")
        ax.set_xlabel("Stock")
        plt.xticks(rotation=45)
        ax.set_ylabel("Yearly Return (%)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig1,use_container_width=True)
    with col2:
        st.markdown("**Top 10 Red Stocks**")
        fig2, ax = plt.subplots()
        ax.plot(df2['Ticker'],df2['Yearly Return'], marker='o', linestyle='-', color='red', label='Yearly Return')
        ax.set_title("📍 Stock Returns with Markers")
        ax.set_xlabel("Stock")
        plt.xticks(rotation=45)
        ax.set_ylabel("Yearly Return (%)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig2,use_container_width=True)
    st.title("Top 10 Green Stocks")
    st.dataframe(df1)
    st.title("Top 10 Red Stocks")
    st.dataframe(df2)
stock()