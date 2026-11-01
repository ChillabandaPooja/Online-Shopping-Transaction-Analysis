# Online Shopping Transaction Analysis System

## Project Overview

The **Online Shopping Transaction Analysis System** is a data analysis project that analyzes online shopping transactions using MySQL and Python.

It retrieves order information from a MySQL database and performs data analysis using Pandas and NumPy. Matplotlib is used to generate visualizations that help understand shopping patterns, payment methods, monthly orders, and product sales.

## Technologies Used

- **MySQL** – Database management and SQL queries
- **Python** – Data analysis and processing
- **Pandas** – Data manipulation and analysis
- **NumPy** – Statistical calculations
- **Matplotlib** – Data visualization

## Project Features

1. Retrieves order details from a MySQL database.
2. Calculates the total number of orders.
3. Identifies delivered orders.
4. Calculates total delivered sales.
5. Calculates average, highest, and lowest order values.
6. Performs statistical analysis using NumPy.
7. Analyzes orders by payment method.
8. Analyzes monthly order volume.
9. Identifies the most-sold products.
10. Generates a transaction summary report.

## Database Structure

The project uses three MySQL tables:

- **products** – Stores product IDs, names, categories, and prices.
- **orders** – Stores order dates, payment methods, and order statuses.
- **order_items** – Stores product quantities and order details.

## Project Structure

```text
Online_Shopping_Analysis/
│
├── main.py
├── .gitignore
├── payment_method_chart.png
├── monthly_orders_chart.png
├── product_sales_chart.png
├── transaction_summary.txt
└── README.md
```

## Visualizations

### 1. Orders by Payment Method

Shows the number of orders made using different payment methods.

### 2. Monthly Order Volume

Displays the number of orders placed each month.

### 3. Product-wise Sales Analysis

Shows the quantities of different products sold in delivered orders.

## How to Run the Project

### 1. Install Python Libraries

```bash
pip install pandas numpy matplotlib mysql-connector-python
```

### 2. Set Up MySQL

Create a MySQL database named `online_shopping` and create the required tables: `products`, `orders`, and `order_items`.

### 3. Configure Database Connection

Set your MySQL password as an environment variable.

For Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="your_mysql_password"
```

For Git Bash:

```bash
export MYSQL_PASSWORD="your_mysql_password"
```

### 4. Run the Python Program

```bash
python main.py
```

The program connects to MySQL, analyzes the transaction data, displays visualizations, and generates a transaction summary report.

## Output Files

- `payment_method_chart.png`
- `monthly_orders_chart.png`
- `product_sales_chart.png`
- `transaction_summary.txt`

## Conclusion

This project demonstrates how SQL and Python can be integrated for analyzing online shopping transactions. It helps identify sales patterns, understand customer payment preferences, and analyze product performance through data analysis and visualization.