import streamlit as st
from Home import home# type: ignore
from Topstock import stock # type: ignore
from Average import avg #type:ignore
from Volume import vol # type: ignore
from Volatility import vol # type: ignore
from Cumulative import cum # type: ignore
from Correlation import corr # type: ignore
from Sector import sec # type: ignore
from Month import mnth # type: ignore
pages = {
    "Main":[st.Page("Home.py",title="🗒Main")],
    " 📊Dashboard": 
    [  
        st.Page("Topstock.py", title="🗒Top 10 Green and Red stocks"),
        st.Page("Average.py", title="🗒Average Price across the stocks"),
        st.Page("Volume.py",title="🗒Average Volume across the stocks"),
        st.Page("Volatility.py",title="🗒Volatility Analysis"),
        st.Page("Cumulative.py", title="🗒Cumulative Return Over Time"),
        st.Page("Correlation.py", title="🗒Stock Price Correlation"),
        st.Page("Sector.py",title="🗒Sector-wise Performance"),
        st.Page("Month.py",title="🗒Month-wise Performance"),
        ]}
pg = st.navigation(pages)
pg.run()