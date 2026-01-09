# Pandas project

import pandas as pd


#csv (services.csv)
df = pd.read_csv(r"C:\Users\Krize Bhattarai\Downloads\Python Class Recordings-20251203T095411Z-1-001\Python Class Recordings\Class 6\services.csv")
# print(df)

# print(df.head())

#Excel(LUSID Excel)
df2 = pd.read_excel(r"C:\Users\Krize Bhattarai\Downloads\Python Class Recordings-20251203T095411Z-1-001\Python Class Recordings\Class 6\LUSID Excel - Setting up your market data.xlsx")
# print(df2)

df3 = pd.read_html(r"https://www.basketball-reference.com/leagues/NBA_2015_totals.html")
# print(df3)
# print(df3[0].head())

df4 = pd.read_csv(r"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(type(df4))

a = df4.dtypes
# print(a)
b = df4.describe() # Provids statistical summary data
# print(b)

c = df4.select_dtypes('object') # only selects strings/text column
# print(c)

d = df4.select_dtypes('int64') # only selects integer columns
# print(d)

#NEW CSV DATA

office = pd.read_csv(r"C:\Users\Krize Bhattarai\Downloads\Python Class Recordings-20251203T095411Z-1-001\Python Class Recordings\Class 6\P1-OfficeSupplies.csv")
top_5 = office.head()
# print(top_5)

office['Sales'] = office['Units'] * office['Unit Price'] # Add another column called sales which is (units * unit price)
# print(office)