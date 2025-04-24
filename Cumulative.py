import pandas as pd
import streamlit as st
import pymysql
import matplotlib.pyplot as plt
from streamlit_extras.metric_cards import style_metric_cards
import math
def cum():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('Select * from stockdataset')
    myresult=mycursor.fetchall()
    df1=pd.DataFrame(myresult,columns=('S.no','Ticker','Close','Date','High','Low','Month','Open','Volume'))
    option=df1['Ticker'].unique()
    stock=st.sidebar.selectbox(label="Filter stock",options=option)
    if stock in option:
        df=df1[df1['Ticker']==stock]
        df["Prev Close"] = df.groupby("Ticker")["Close"].shift(1)
        df["Daily Return"] = (df["Close"] - df["Prev Close"]) / df["Prev Close"]
        df["Daily Return"].fillna(0, inplace=True)
        df["Cumulative Return"] = (1 + df["Daily Return"]).groupby(df["Ticker"]).cumprod() - 1
        final_returns = df.groupby("Ticker").tail(1)[["Ticker", "Cumulative Return"]]
        top_5 = final_returns.sort_values(by="Cumulative Return", ascending=False).head(5)
        ticker = stock
        cumulative_return = top_5["Cumulative Return"]
        col1,col2=st.columns(2)
        with col1:
            val=math.floor(cumulative_return*100.0)/100.0
            st.metric(f"{ticker}", value=val)
            style_metric_cards(background_color="light blue", border_left_color="#4CAF50", border_color="#e0e0e0")
        with col2:
            df =df.pivot(index="Date", columns="Ticker", values="Cumulative Return")
            st.subheader("🏆 Cumulative Return for Top 5 Performing Stocks")
            fig, ax = plt.subplots()
            df.plot(ax=ax, linewidth=2)
            ax.set_title("Top 5 Stocks by Cumulative Return")
            ax.set_ylabel("Cumulative Return")
            ax.set_xlabel("Date")
            plt.xticks(rotation=90)
            ax.legend(title="Ticker")
            st.pyplot(fig)
cum()