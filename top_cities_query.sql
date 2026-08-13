SELECT TOP 10
    c.customer_city,
    SUM(oi.price) AS total_sales,
    COUNT(o.order_id) AS total_orders,
    (SUM(oi.price) / COUNT(o.order_id)) AS avg_order_value
FROM olist_orders_dataset AS o
JOIN olist_customers_dataset AS c 
    ON o.customer_id = c.customer_id
JOIN olist_order_items_dataset AS oi 
    ON o.order_id = oi.order_id
GROUP BY c.customer_city
ORDER BY total_sales DESC;
