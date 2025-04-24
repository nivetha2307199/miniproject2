import pandas as pd
import streamlit as st
import pymysql
import plotly.express as px
def vol():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('Select * from stockdataset')
    myresult=mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=('S.no','Ticker','Close','Date','High','Low','Month','Open','Volume'))
    df["Prev Close"] = df.groupby("Ticker")["Close"].shift(1)
    df["Daily Return"] = (df["Close"] - df["Prev Close"]) / df["Prev Close"]
    df.dropna(subset=["Daily Return"], inplace=True)
    volatility_df = df.groupby("Ticker")["Daily Return"].std().reset_index()
    volatility_df.columns = ["Ticker", "Volatility"]
    top_10 = volatility_df.sort_values(by="Volatility",ascending=False,ignore_index=True)
    st.title("Volatility Analysis")
    fig=px.line(volatility_df,x="Ticker",y="Volatility")
    st.plotly_chart(fig)
    st.title("Data view for top 10")
    st.dataframe(top_10.head(10))
vol()