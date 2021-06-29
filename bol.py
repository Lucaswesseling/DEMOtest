import pandas as pd
import numpy as np

# file_wk13 = r"W:\Maarten\iri_weekrapport_week13.csv"
# df1 = pd.read_csv(file_wk13, sep=';', encoding = "ISO-8859-1")

# file_Q1 = r"W:\Martijn\bol.com\iri_weekrapport_2020Q1.csv"
# df1 = pd.read_csv(# file_Q1, sep=';', encoding = "ISO-8859-1")

# file_Q2 = r"W:\Martijn\bol.com\iri_weekrapport_2020Q2.csv"
# df2 = pd.read_csv(# file_Q2, sep=';', encoding = "ISO-8859-1")

# file_Q3 = r"W:\Martijn\bol.com\iri_weekrapport_2020Q3.csv"
# df3 = pd.read_csv(# file_Q3, sep=';', encoding = "ISO-8859-1")

# file_Q4 = r"W:\Martijn\bol.com\iri_weekrapport_2020Q4.csv"
# df4 = pd.read_csv(# file_Q4, sep=';', encoding = "ISO-8859-1")

# df5 = df1.append(df2).append(df3).append(df4)
# df5['amtOrderedInclVat'] = df5['amtOrderedInclVat'].str.replace(',', '').astype(float)
# df = df5.groupby(['week', 'chunkName']).agg({
#                              'yrWeekNo': 'last',
#                              'chunkId':'last',
#                              'productSubSubGroup':'last',
#                              'qtyOrdered': np.sum,
#                              'amtOrderedInclVat':np.sum}).reset_index()
#
# df['yrWeekNo'] = df['yrWeekNo'].astype(str).str[:4]
# df['Time'] = "Wk " + df['week'].astype(str) + ", " + df['yrWeekNo'].astype(str)
# df = df[['Time', 'productSubSubGroup', 'chunkName', 'chunkId', 'qtyOrdered', 'amtOrderedInclVat']]
# df.to_csv(r"C:\Users\zanm\OneDrive - IRI\bol_data.csv", index=False, header=True)

# file_link = r"C:\Users\wesl\OneDrive - IRI\Bol.com\Bol_IRI_link.xlsx"
# file_Bol = r"C:\Users\wesl\OneDrive - IRI\Bol.com\Bol_data.xlsx"
# df1 = pd.read_excel(file_link)
# df2 = pd.read_excel(file_Bol)

file_link = r"C:\Users\wesl\OneDrive - IRI\Bol.com\Ex_1.xlsx"
file_Bol = r"C:\Users\wesl\OneDrive - IRI\Bol.com\Ex_2.xlsx"
df1 = pd.read_excel(file_link)
df2 = pd.read_excel(file_Bol)

print (df1)
print (df2)