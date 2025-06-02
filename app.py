import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Analysis – Köksglädje", layout="wide")

@st.cache_data
def load_data():
    conn = sqlite3.connect("Köksglädje.db")
    products = pd.read_sql("SELECT * FROM Products", conn)
    transaction_details = pd.read_sql("SELECT * FROM TransactionDetails", conn)
    transactions = pd.read_sql("SELECT * FROM Transactions", conn)
    conn.close()
    return products, transaction_details, transactions

products, transaction_details, transactions = load_data()

# Merge transaction details with transactions for date and store info
df = transaction_details.merge(transactions[['TransactionID', 'StoreID', 'TransactionDate']], on='TransactionID', how='left')

# Date processing
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
df['Year'] = df['TransactionDate'].dt.year
df['Month'] = df['TransactionDate'].dt.to_period('M').astype(str)

# Calculate total sales
df['TotalSales'] = df['Quantity'] * df['PriceAtPurchase']

st.title("📊 Dashboard för försäljningsanalys – Köksglädje")
st.markdown("Analys av lageroptimering, lågomsättningsprodukter och försäljningstrender.")

# Section 1: Total sales per store for 2023
st.header("🏬 Total sales per store (2023)")
sales_2023 = df[df['Year'] == 2023]
sales_per_store = sales_2023.groupby("StoreID")["TotalSales"].sum().sort_values(ascending=False)
st.bar_chart(sales_per_store)

# Section 2: Total sales per product (sorted)
st.header("📊 Total sales per product")
total_sales_by_product = df.groupby('ProductID')['TotalSales'].sum().reset_index()
total_sales_by_product = total_sales_by_product.sort_values(by='TotalSales', ascending=False)
total_sales_by_product = total_sales_by_product.merge(products[['ProductID', 'ProductName']], on='ProductID', how='left')

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(total_sales_by_product['ProductName'], total_sales_by_product['TotalSales'], color='skyblue')
ax.set_title('Total sales per product')
ax.set_xlabel('Product')
ax.set_ylabel('Total Sales (SEK)')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Section 3: Monthly sales trends per product
st.header("📈 Monthly sales trends per product")

monthly_sales = df.groupby(['Month', 'ProductID'])['TotalSales'].sum().reset_index()
monthly_sales = monthly_sales.merge(products[['ProductID', 'ProductName']], on='ProductID', how='left')
pivot_table = monthly_sales.pivot(index='Month', columns='ProductName', values='TotalSales').fillna(0)

fig2, ax2 = plt.subplots(figsize=(14,6))
pivot_table.plot(marker='o', ax=ax2)
ax2.set_title('Monthly total sales per product')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Sales (SEK)')
plt.xticks(rotation=45)
ax2.legend(title='Product Name', bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig2)

# Section 4: Low sales products
st.header("🔻 Products with low sales")
low_sales_threshold = total_sales_by_product['TotalSales'].quantile(0.25)
low_sales = total_sales_by_product[total_sales_by_product['TotalSales'] < low_sales_threshold]
st.dataframe(low_sales[['ProductName', 'TotalSales']].rename(columns={'TotalSales': 'Total Sales (SEK)'}))

# Conclusions
st.header("📌 Conclusions and Business Insights")
st.markdown("""
- 📦 **Inventory Optimization**: Focus on the best-selling products to plan smarter purchases.
- 🔍 **Low Sales Products**: Consider discounts or removing low-performing products.
- 📊 **Sales Trends**: Identify seasonal patterns to optimize marketing and stock decisions.
""")
