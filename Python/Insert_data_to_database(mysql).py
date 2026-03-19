import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("D:\\Data_set\\Data_set_13\\Data\\Superstore.txt")
df.columns = df.columns.str.replace(' ','_')
conn = create_engine('mysql+pymysql://root:Vivek%40123@127.0.0.1:3306/sales_data')
df.to_sql('sales', conn, index=False, if_exists='replace')
df.to_sql(
    'sales',
    conn,
    index=False,
    if_exists='replace',
    chunksize=1000,
    method='multi'
)