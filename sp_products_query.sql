SELECT TOP 10
    p.product_category_name,
    SUM(oi.price) AS category_sales,
    COUNT(oi.product_id) AS items_sold
FROM olist_orders_dataset AS o
JOIN olist_customers_dataset AS c 
    ON o.customer_id = c.customer_id
JOIN olist_order_items_dataset AS oi 
    ON o.order_id = oi.order_id
JOIN olist_products_dataset AS p 
    ON oi.product_id = p.product_id
WHERE c.customer_city = 'sao paulo'
    AND o.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY category_sales DESC;
