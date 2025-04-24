import pandas as pd
import streamlit as st
import math
import pymysql
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
def avg():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('Select * from stockdataset')
    myresult=mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=('S.no','Ticker','Close','Date','High','Low','Month','Open','Volume'))
    option = df['Ticker'].unique()
    stocks=st.sidebar.selectbox(label="Filter Stocks",options=option)
    st.title("The Average price across all stocks")
    if stocks in option:
        filtered_df = df[df['Ticker'] == stocks]
        midpoint = len(filtered_df) // 2
        current=filtered_df['Close'].iloc[:midpoint].mean()
        previous=filtered_df['Close'].iloc[midpoint:].mean()
        avg_close = filtered_df['Close'].astype(float).mean()
        change=current-previous
        per_change=(change/previous)*100
        col1,col2=st.columns(2)
        with col1:
            avg=math.floor(avg_close*100.0)/100.0
            per_change=math.floor(per_change*100.0)/100.0
            st.metric(label="Average Close Price", value=avg, delta=per_change)
            style_metric_cards(background_color="#f9f9f9", border_left_color="#4CAF50", border_color="#e0e0e0")
        with col2:
            df=df.groupby('Ticker')['Close'].mean()
            df = df.to_frame()
            df.rename(columns={'Close': 'Average Price'}, inplace=True)
            df=df.head(10)
            fig = px.bar(
                df,
                y='Average Price',
                title='Average Close Price per Stock',
                color='Average Price',
                color_continuous_scale='Blues'
            )

            st.plotly_chart(fig,use_container_width=False)
avg()