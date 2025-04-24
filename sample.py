from pathlib import Path
import pandas as pd
import os
import yaml
p = Path(r"C:\Users\NIVI\Downloads\data\2023-12")
maindata=[]
for subdir in p.iterdir():
    with open(subdir,'r') as yaml_file:
        data=(yaml.safe_load(yaml_file))
        maindata.append(data)
t=[]
c=[]
d=[]
h=[]
l=[]
m=[]
o=[]
v=[]
for i in maindata:
    for j in i:
        data=list(j.values())
        t.append(data[0])
        c.append(data[1])
        d.append(data[2])
        h.append(data[3])
        l.append(data[4])
        m.append(data[5])
        o.append(data[6])
        v.append(data[7])
dict_data={'Ticker':t,'Close':c,'Date':d,'High':h,'Low':l,'Month':m,'Open':o,'Volume':v}
pd.options.display.max_rows=20000
df=pd.DataFrame(dict_data)
path_src=r"C:\Users\NIVI\OneDrive\Documents\AIML Course\MiniProject2\2023-12"
os.makedirs(path_src, exist_ok=True)
index=1
for file,grp in df.groupby(['Ticker']):
    file=str(file)
    file=(file[2:len(file)-3])+"_"+str(index)
    file_name= f"{file}.csv"
    file_path = os.path.join(path_src,file_name)
    grp.to_csv(file_path, index=False)
    print(f"Saved: {file_path}")
    index+=1