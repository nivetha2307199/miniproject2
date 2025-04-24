import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
def mnth():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('select s.Ticker,c.sector,s.Close,s.Month,s.Date from stockdataset s JOIN sector_data c on S.Ticker=c.COMPANY ')
    myresult=mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=["Company","Sector","Close","Month","Date"])
    df = df.sort_values(by=['Sector', 'Date'])
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_df = df.groupby(['Sector', 'Month'])['Close'].last().reset_index()
    monthly_df['prev_close'] = monthly_df.groupby('Sector')['Close'].shift(1)
    monthly_df['monthly_return'] = (monthly_df['Close'] - monthly_df['prev_close']) / monthly_df['prev_close'] * 100
    monthly_df = monthly_df.dropna(subset=['monthly_return'])
    st.title("📈 Top 5 Gainers and Losers by Month")
    months = monthly_df['Month'].unique()
    month=st.sidebar.selectbox(label="Filter Months",options=months)
    if(month in months):
        st.subheader(f"📅 {month}")
        df_month = monthly_df[monthly_df['Month'] == month]
        top_5 = df_month.nlargest(4, 'monthly_return')
        bottom_5 = df_month.nsmallest(4, 'monthly_return')
        col1, col2 = st.columns(2)
        with col1:
            fig1 = px.bar(top_5, x='Sector', y='monthly_return', color='Sector',
                        labels={'monthly_return': 'Return (%)'}, title='Top Gainers')
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            fig2 = px.bar(bottom_5, x='Sector', y='monthly_return', color='Sector',
                        labels={'monthly_return': 'Return (%)'}, title='Top Losers')
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("Chose it")

mnth()