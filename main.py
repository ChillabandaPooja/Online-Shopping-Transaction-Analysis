import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL
import os

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="online_shopping"
)
print("Successfully connected to MySQL!")

# Fetch order details
query = """
SELECT
    o.order_id,
    o.order_date,
    o.payment_method,
    o.order_status,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY
    o.order_id,
    o.order_date,
    o.payment_method,
    o.order_status
"""

df = pd.read_sql(query, conn)

print("\nOrder Details:")
print(df)
# Data Analysis using Pandas

print("\n----- Transaction Analysis -----")

# Total number of orders
total_orders = df["order_id"].nunique()
print("Total Orders:", total_orders)

# Filter delivered orders
delivered = df[df["order_status"] == "Delivered"]

# Total delivered orders
delivered_orders = delivered["order_id"].nunique()
print("Delivered Orders:", delivered_orders)

# Total sales
total_sales = delivered["order_total"].sum()
print("Total Sales:", total_sales)

# Average Order Value
aov = delivered["order_total"].mean()
print("Average Order Value:", aov)

# Highest order value
highest = delivered["order_total"].max()
print("Highest Order Value:", highest)

# Lowest order value
lowest = delivered["order_total"].min()
print("Lowest Order Value:", lowest)

# NumPy calculations
print("\n----- NumPy Statistics -----")

values = delivered["order_total"].to_numpy()

print("Mean:", np.mean(values))
print("Median:", np.median(values))
print("Standard Deviation:", np.std(values))
# Payment Method Analysis

payment_counts = df["payment_method"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(payment_counts.index, payment_counts.values)

plt.title("Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("payment_method_chart.png")
plt.show()
# Monthly Order Volume Analysis

# Monthly Order Volume Analysis

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

df = df.dropna(subset=["order_date"])

monthly_orders = df.groupby(
    df["order_date"].dt.to_period("M")
)["order_id"].nunique()

plt.figure(figsize=(8, 5))

plt.plot(
    monthly_orders.index.astype(str),
    monthly_orders.values,
    marker="o"
)

plt.title("Monthly Order Volume")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_orders_chart.png")
plt.show()
# Product-wise Sales Analysis

product_query = """
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
JOIN orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'Delivered'
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
"""

product_df = pd.read_sql(product_query, conn)

print("\n----- Product Sales Analysis -----")
print(product_df)

plt.figure(figsize=(9, 5))

plt.bar(
    product_df["product_name"],
    product_df["total_quantity_sold"]
)

plt.title("Product-wise Sales Analysis")
plt.xlabel("Product Name")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales_chart.png")
plt.show()
# Final Transaction Summary Report

print("\n================================")
print("   ONLINE SHOPPING TRANSACTION REPORT")
print("================================")

print("Total Orders:", df["order_id"].nunique())

print("\nOrder Status Summary:")
print(df["order_status"].value_counts())

delivered = df[df["order_status"] == "Delivered"]

total_sales = delivered["order_total"].sum()
average_order_value = delivered["order_total"].mean()

print("\nTotal Delivered Sales: Rs.", round(total_sales, 2))
print("Average Order Value: Rs.", round(average_order_value, 2))

print("\n================================")
print("       END OF REPORT")
print("================================")
with open("transaction_summary.txt", "w") as file:
    file.write("ONLINE SHOPPING TRANSACTION REPORT\n")
    file.write("----------------------------------\n")
    file.write(f"Total Orders: {df['order_id'].nunique()}\n")
    file.write(f"Delivered Orders: {len(delivered)}\n")
    file.write(f"Total Delivered Sales: Rs. {total_sales:.2f}\n")
    file.write(f"Average Order Value: Rs. {average_order_value:.2f}\n")
conn.close()