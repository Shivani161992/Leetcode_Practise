import pandas as pd
x=pd.read_csv(r'C:\Users\toshi\Desktop\lab\ABR_MDTemplate_Rachal.csv')
a=x.loc[x['vdts'] != 'FALSE']

print(x)