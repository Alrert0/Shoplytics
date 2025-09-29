# Shoplytics

## Overview  
Shoplytics is an educational project for analyzing e-commerce data using PostgreSQL and Python.  
The goal of the project is to explore customer behavior, order trends, and product profitability through SQL queries, data visualizations, and Excel exports.  

The project includes:  
- SQL queries with `JOIN` for relational analysis  
- 6 types of data visualizations (`matplotlib`)  
- An interactive timeline chart (`plotly`)  
- Excel reports with formatting (`openpyxl`)  

---

## Database Structure  

Main tables:  
1. `customers` – customer information  
2. `orders` – order details  
3. `order_items` – products within orders  
4. `products` – product information  
5. `sellers` – seller information  
6. `order_payments` – payment details  

---

## Relationships  
- `customers.customer_id` ↔ `orders.customer_id`  
- `orders.order_id` ↔ `order_items.order_id`  
- `order_items.product_id` ↔ `products.product_id`  
- `order_items.seller_id` ↔ `sellers.seller_id`  
- `orders.order_id` ↔ `order_payments.order_id`  

---

## ERD
  <img width="1013" height="906" alt="Снимок экрана 2025-09-21 164755" src="https://github.com/user-attachments/assets/d61e82be-440c-4316-bc36-298ab507e4fa" />


## Tools & Resources  

- **PostgreSQL** – main relational database  
- **pgAdmin / DBeaver** – database management tools (optional)  
- **Python 3.10** – for running SQL queries from scripts  
- **psycopg2** – Python library to connect with PostgreSQL  
- **Git & GitHub** – version control and project hosting  
- **Dataset** – public e-commerce dataset (~100k rows, multiple tables)

  ---

## Implemented Features  

### Visualizations (Matplotlib)  
- Pie chart — distribution of orders by state  
- Bar chart — average delivery cost by state (Top-10)  
- Horizontal bar chart — top-10 categories by revenue  
- Line chart — number of orders by month  
- Histogram — product price distribution  
- Scatter plot — product price vs delivery cost  

_All charts are saved in `/charts/`._  

### Interactive Chart (Plotly)  
- Orders by month with a time range slider  
- Interactive buttons: last 3 months, 6 months, 1 year, all time  

### Excel Export (openpyxl)  
- Multi-sheet reports  
- Frozen headers  
- Auto filters on all columns  
- Conditional formatting with gradient colors  
- Highlighting of minimums and maximums  

##  How to Run the Project

1. **Install PostgreSQL** on your computer.  
2. **Create a database**  
3. **Import the dataset** into the database 
4. **Run the SQL queries** from `queries.sql` to check and analyze the data.  
5. **Run the Python script** `main.py` to connect to the database and execute some queries automatically.  



