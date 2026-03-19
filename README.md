# 🛒 Superstore Sales Data Analysis

A complete end-to-end data analysis project on the Superstore retail dataset — covering data ingestion, SQL querying, Python EDA, and Power BI visualization across 4 fiscal years (2014–2017).

---

## 📁 Project Structure

```
├── Superstore.csv                        # Raw dataset (9,994 records)
├── Insert_data_to_database(mysql).py     # Load CSV data into MySQL
├── query.sql                             # SQL business queries
├── EDA.py                                # Python exploratory data analysis
└── Dashbored.pbix                        # Power BI dashboard
```

---

## 📊 Dataset Overview

| Field | Detail |
|---|---|
| Source | Superstore.csv |
| Records | 9,994 rows |
| Columns | 21 |
| Period | January 2014 – December 2017 |
| Coverage | Sales, Profit, Discount, Region, Category, Customer, Shipping |

---

## 🛠️ Tech Stack

- **Python** — Pandas, Matplotlib, Seaborn, SQLAlchemy
- **MySQL** — Data storage and SQL querying
- **Power BI** — Interactive dashboard (`.pbix`)
- **PyMySQL** — MySQL connector for Python

---

## ⚙️ Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/superstore-analysis.git
cd superstore-analysis
```

### 2. Install Python Dependencies
```bash
pip install pandas matplotlib seaborn sqlalchemy pymysql
```

### 3. Set Up MySQL Database
Create a database named `sales_data` in your MySQL server:
```sql
CREATE DATABASE sales_data;
```

### 4. Load Data into MySQL
```bash
python "Insert_data_to_database(mysql).py"
```
> ⚠️ Update the connection string in the script with your own MySQL credentials before running.

### 5. Run SQL Queries
Open `query.sql` in MySQL Workbench or any SQL client and execute the queries against the `sales_data` database.

### 6. Run Python EDA
```bash
python EDA.py
```
> ⚠️ Update the MySQL connection string in `EDA.py` with your own credentials before running.

### 7. Open Power BI Dashboard
Open `Dashbored.pbix` in **Power BI Desktop** and refresh the data source to connect to your local MySQL instance.

---

## 🔍 SQL Analysis Highlights

| Query | Insight |
|---|---|
| Top Revenue Segment | West + Technology delivered the highest revenue |
| Discount Impact | High discounts (>20%) yield avg -$97 loss per order |
| Monthly Trends | Q4 (Nov–Dec) consistently peaks every year |
| Loss-Making Categories | Furniture (Tables: -$17,726) loses despite high sales |
| Top Customers | Sean Miller tops revenue but generates negative profit |

---

## 📈 Key Findings

- 💰 **Total Sales:** $2,297,201 &nbsp;|&nbsp; **Total Profit:** $286,397 &nbsp;|&nbsp; **Margin:** 12.5%
- 📦 **Best Category:** Technology (17.4% margin)
- ⚠️ **Worst Category:** Furniture (2.5% margin)
- 🌍 **Top Region:** West ($725K sales, 14.9% margin)
- 🔻 **Biggest Loss Driver:** High discounts (>20%) — total loss of -$135,376
- 📅 **Growth:** Sales grew 51% from 2014 to 2017

---

## 📉 EDA Charts Generated

- Sales by Region & Category (grouped bar chart)
- Annual Sales & Profit Trend (2014–2017)
- Average Profit by Discount Level
- Category Sales vs Profit Margin
- Sales Distribution by Ship Mode (pie chart)
- Profit by Sub-Category (horizontal bar chart)

---

## 🔒 Security Note

The MySQL connection strings in `EDA.py` and `Insert_data_to_database(mysql).py` contain hardcoded credentials. **Before pushing to GitHub:**

1. Replace credentials with environment variables or a `.env` file
2. Add `.env` to your `.gitignore`

```python
# Recommended approach
import os
conn = create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@localhost:3306/sales_data")
```

---

## 📄 License

This project is for educational and portfolio purposes. The Superstore dataset is a publicly available sample dataset.
