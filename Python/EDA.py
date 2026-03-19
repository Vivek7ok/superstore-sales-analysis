import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import numpy as np
import matplotlib.patches as mpatches

conn = create_engine('mysql+pymysql://root:Vivek%40123@127.0.0.1:3306/sales_data')
query = 'select * from sales'
df = pd.read_sql(query,conn)

def discount_level(x):
    if x == 0:
        return 'No Discount'
    elif 0 < x <= 0.10:
        return 'Low Discount'
    elif 0.10 < x <= 0.20:
        return 'Medium Discount'
    else:
        return 'Big Discount'

df['Discount_level'] = df['Discount'].apply(discount_level)

print(df.head())
print(df.columns)

fig, axis = plt.subplots(2, 2, figsize=(14, 10))

# 1️⃣ Sales by Region
sns.barplot(
    data=df, x='Region', y='Sales', hue='Category',
    palette='Set2',
    ax=axis[0, 0]
)
axis[0, 0].set_title('Sales by Region')

# 2️⃣ Sales by Country
sns.barplot(
    data=df, x='Country', y='Sales', hue='Category',
    palette='Set1',
    ax=axis[0, 1]
)
axis[0, 1].set_title('Sales by Country')

# 3️⃣ Profit by Discount Level
sns.lineplot(
    data=df, x='Discount_level', y='Profit',
    marker='o', linewidth=2.5,
    color='purple',
    ax=axis[1, 0]
)
axis[1, 0].set_title('Profit by Discount Level')

# 4️⃣ Pie Chart - Ship Mode
ship_sales = df.groupby('Ship_Mode')['Sales'].sum()

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

axis[1, 1].pie(
    ship_sales,
    labels=ship_sales.index,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140
)

axis[1, 1].set_title('Sales by Ship Mode')
axis[1, 1].axis('equal')  # keep circle shape

# Adjust spacing
plt.tight_layout()
plt.show()