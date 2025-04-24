import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def corr():
    mydb=pymysql.connect(host='localhost',user='root',password='root@2024',database='stockanalysis')
    mycursor=mydb.cursor()
    mycursor.execute('select Ticker,Close,High,Low,Open,Volume from stockdataset')
    myresult=mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=('Ticker','Close','High','Low','Open','Volume'))
    stock=st.sidebar.multiselect(label="Filter Sector",options=df['Ticker'].unique())
    if stock:
        df = df[df['Ticker'].isin(stock)]
        df1 = df.select_dtypes(include='number')
        pct_change = df1.pct_change().dropna()
        correlation_matrix = pct_change.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        st.title("Correlation Analysis")
        name=f"{stock}"
        st.subheader(name)
        st.subheader("Heatmap of Correlation Matrix")
        st.pyplot(plt)
        st.subheader("Correlation Matrix")
        st.dataframe(correlation_matrix)

    else:
        st.info("Please select one or more months from the sidebar.")
corr()