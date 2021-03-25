import pandas as pd

df = pd.read_excel(r'/Users/shivani/Desktop/HCCTransposeProblem.xlsx')  # read exel file
#
df1 = df.head(6) # take first 6 rows
df1.drop(df1.columns[0], axis=1, inplace=True) #remove first Input column
dfIndexColumn = df1.iloc[:, 0:2] # take Memberid and Activity Year in a seperate DF
dfValueColumn = df1.iloc[:, 2:12].astype(int) # Convert all HCC columns into Integer
dfData = dfIndexColumn.join(dfValueColumn) #Merge  dfIndexColumn and dfValueColumn

dfData = dfData.set_index(['MemberID', 'ActivityYear']) #set index for Memberid and Activity Year
dfdat = dfData.dot(dfData.columns + ',').str.rstrip(',').reset_index(name='HCC') # create column HCC and get header as a value whereever column value is 1
dfdat['HCC'] = dfdat['HCC'].map(lambda x: ','.join([x.strip('HCC0') for x in x.split(',')])) # split string by comma. From each element remove HCC0 and join string by comma

print(dfdat)
