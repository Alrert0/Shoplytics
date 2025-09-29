import psycopg2
import pandas as pd
from tabulate import tabulate

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="Project",
        user="postgres",
        password="0000",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    print("✅ Успешное подключение к PostgreSQL")

    # Список запросов
    queries = [
        (
            "1. Find the most expensive product per product_id",
            """
            SELECT product_id, MAX(price) 
            FROM order_items 
            GROUP BY product_id;
            """
        ),
        (
            "2. Total payment value grouped by payment type",
            """
            SELECT payment_type, SUM(payment_value) 
            FROM order_payments 
            GROUP BY payment_type;
            """
        ),
        (
            "3. Count number of orders by customer state",
            """
            SELECT c.customer_state, COUNT(*)
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            GROUP BY c.customer_state;
            """
        ),
        (
            "4. Count number of products in each category",
            """
            SELECT product_category_name, COUNT(*) 
            FROM products 
            GROUP BY product_category_name;
            """
        ),
        (
            "5. Calculate total order value (items + freight) per order",
            """
            SELECT order_id, SUM(price + freight_value) AS total
            FROM order_items
            GROUP BY order_id;
            """
        ),
        (
            "6. Top 10 sellers by total sales value",
            """
            SELECT s.seller_id, s.seller_city, SUM(oi.price) AS total_sales
            FROM order_items oi
            JOIN sellers s ON oi.seller_id = s.seller_id
            GROUP BY s.seller_id, s.seller_city
            ORDER BY total_sales DESC
            LIMIT 10;
            """
        ),
        (
            "7. Average delivery time (purchase → customer delivery) by state",
            """
            SELECT c.customer_state, 
                   AVG(o.order_delivered_customer_date - o.order_purchase_timestamp) AS avg_delivery_time
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            WHERE o.order_delivered_customer_date IS NOT NULL
            GROUP BY c.customer_state
            ORDER BY avg_delivery_time;
            """
        ),
        (
            "8. Product categories with the highest average item price",
            """
            SELECT p.product_category_name, AVG(oi.price) AS avg_price
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            GROUP BY p.product_category_name
            ORDER BY avg_price DESC
            LIMIT 10;
            """
        ),
        (
            "9. Top 10 customers by total spending (items + freight)",
            """
            SELECT c.customer_unique_id, SUM(oi.price + oi.freight_value) AS total_spent
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY c.customer_unique_id
            ORDER BY total_spent DESC
            LIMIT 10;
            """
        ),
        (
            "10. Correlation between review scores and response times",
            """
            SELECT r.review_score, 
                   AVG(r.review_answer_timestamp - r.review_creation_date) AS avg_response_time
            FROM order_reviews r
            WHERE r.review_answer_timestamp IS NOT NULL
            GROUP BY r.review_score
            ORDER BY r.review_score;
            """
        )
    ]

    # Выполняем запросы и выводим в виде таблицы
    for i, (desc, q) in enumerate(queries, start=1):
        print(f"\n▶ Query {i}: {desc}")
        df = pd.read_sql(q, conn)  # сразу в DataFrame
        print(tabulate(df, headers='keys', tablefmt='psql'))

    # Закрываем соединение
    cur.close()
    conn.close()
    print("\n🔒 Соединение закрыто")

except Exception as e:
    print("❌ Ошибка при подключении:", e)
