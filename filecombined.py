#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from pathlib import Path
import pandas as pd
p = Path("C:/Users/NIVI/OneDrive/Documents/AIML Course/MiniProject2")
index=10
dataset=[]
cmpy="ADANIENT_1.csv"
year="2023-"
for i in range(1,15):
    val= f"{index}"
    if(index<12 and index>=10 and year=="2023-"):
        s1="2023-"+val
    elif(index==12 and year=="2023-"):
        s1="2023-"+val
        year="2024-"
        index=0
    else:
        if(index<=9):
            s1="2024-0"+val
        elif(index>=10):
            s1=year+val
    index+=1
    path = os.path.join(p,s1,cmpy)
    clean_path = path.replace("\\", "/")
    genre_data = pd.read_csv(clean_path)
    dataset.append(genre_data)
try:
    combined_dataset = pd.concat(dataset, ignore_index=True)
    combined_dataset.to_csv(r"C:\Users\NIVI\OneDrive\Documents\AIML Course\Dataset\ADANIENT.csv")
    print("CSV files combined successfully!")
except:
    print("FileNotFoundError")


# In[ ]:




