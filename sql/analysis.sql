-- COFFEE SALES ANALYSIS (2025)
-- Author: Hassan Akhter

-- 1. Daily Revenue
SELECT 
    DATE(order_timestamp) AS order_date,
    ROUND(SUM(quantity * price),0) AS daily_revenue
FROM orders
JOIN order_items
	ON orders.order_id = order_items.order_id
JOIN products 
	ON order_items.product_id = products.product_id
GROUP BY order_date
--HAVING DATE(order_timestamp) BETWEEN '2025-01-01' AND '2025-06-30'
ORDER BY order_date;

-- 2. MONTHLY REVENUE TREND

SELECT
    DATE(DATE_TRUNC('month', orders.order_timestamp)) AS month,
    ROUND(SUM(order_items.quantity * products.price),0) AS revenue
FROM orders
JOIN order_items  
	ON orders.order_id = order_items.order_id
JOIN products  ON order_items.product_id = products.product_id
GROUP BY month
ORDER BY month;

-- 3. TOP 10 BEST-SELLING PRODUCTS
SELECT
    product_name,
    SUM(order_items.quantity) AS total_units_sold
FROM order_items
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.product_name
ORDER BY total_units_sold DESC
LIMIT 10;

-- 4. REVENUE BY PRODUCT CATEGORY
SELECT
    products.category,
    SUM(order_items.quantity * products.price) AS revenue
FROM order_items
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.category
ORDER BY revenue DESC;

-- 5. STORE-LEVEL REVENUE RANKING
SELECT
    stores.store_id,
    stores.city,
    stores.country,
    ROUND(SUM(quantity * price),0) AS revenue
FROM stores
JOIN orders 
	ON stores.store_id = orders.store_id
JOIN order_items 
	ON orders.order_id = order_items.order_id
JOIN products 
	ON order_items.product_id = products.product_id
GROUP BY stores.store_id, stores.city, stores.country
ORDER BY revenue DESC;

-- 6. PEAK ORDERING HOURS
SELECT
    EXTRACT(HOUR FROM order_timestamp) AS hour,
    COUNT(*) AS order_count
FROM orders
GROUP BY hour
ORDER BY hour;

-- 7. CUSTOMER LIFETIME VALUE (TOP 20)
SELECT
    customers.customer_id,
    customers.name,
    customers.loyalty_tier,
    ROUND(SUM(order_items.quantity * products.price),0) AS lifetime_value
FROM customers 
JOIN orders  
	ON customers.customer_id = orders.customer_id
JOIN order_items 
	ON orders.order_id = order_items.order_id
JOIN products  ON order_items.product_id = products.product_id
GROUP BY customers.customer_id, customers.name, customers.loyalty_tier
ORDER BY lifetime_value DESC
LIMIT 20;

-- 8. AVERAGE BASKET SIZE
SELECT
    ROUND(AVG(item_count),0) AS avg_items_per_order
FROM (
    SELECT
        order_id,
        SUM(quantity) AS item_count
    FROM order_items
    GROUP BY order_id
) t;

-- 9. SEASONAL DRINK PERFORMANCE (PUMPKIN SPICE LATTE)
SELECT
    DATE(DATE_TRUNC('month', orders.order_timestamp)) AS month,
    SUM(order_items.quantity) AS units_sold
FROM order_items 
JOIN orders  ON order_items.order_id = orders.order_id
WHERE order_items.product_id = 25
GROUP BY month
ORDER BY month;

-- 10. REPEAT CUSTOMER RATE
WITH order_counts AS (
    SELECT customer_id, COUNT(*) AS num_orders
    FROM orders
    GROUP BY customer_id
)
SELECT
    SUM(CASE WHEN num_orders > 1 THEN 1 ELSE 0 END)::DECIMAL
        / COUNT(*) AS repeat_customer_rate
FROM order_counts;

-- 11. REVENUE BY LOYALTY TIER
SELECT
    customers.loyalty_tier,
    ROUND(SUM(order_items.quantity * products.price),0) AS revenue
FROM customers
JOIN orders
	ON customers.customer_id = orders.customer_id
JOIN order_items 
	ON orders.order_id = order_items.order_id
JOIN products
	ON order_items.product_id = products.product_id
GROUP BY customers.loyalty_tier
ORDER BY revenue DESC;

-- 12. TOP 10 CUSTOMERS BY NUMBER OF ORDERS
SELECT
    customers.customer_id,
    customers.name,
    COUNT(orders.order_id) AS total_orders
FROM customers 
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
ORDER BY total_orders DESC
LIMIT 10;

-- 13. TOP 10 CUSTOMERS BY REVENUE
SELECT
    customers.customer_id,
    customers.name,
    ROUND(SUM(order_items.quantity * products.price),0) AS revenue
FROM customers 
JOIN orders 
	ON customers.customer_id = orders.customer_id
JOIN order_items  
	ON orders.order_id = order_items.order_id
JOIN products  ON order_items.product_id = products.product_id
GROUP BY customers.customer_id, customers.name
ORDER BY revenue DESC
LIMIT 10;

-- 14. STORE REVENUE BY MONTH

SELECT
    stores.store_id,
    stores.city,
    DATE(DATE_TRUNC('month', orders.order_timestamp)) AS month,
    ROUND(SUM(order_items.quantity * products.price),0) AS revenue
FROM stores 
JOIN orders 
	ON stores.store_id = orders.store_id
JOIN order_items 
	ON orders.order_id = order_items.order_id
JOIN products  
	ON order_items.product_id = products.product_id
GROUP BY stores.store_id, stores.city, month
ORDER BY stores.store_id, month;


-- 15. TOP PRODUCTS BY COUNTRY
SELECT
    stores.country,
    products.product_name,
    ROUND(SUM(order_items.quantity),0) AS units_sold,
    RANK() OVER (PARTITION BY stores.country ORDER BY SUM(order_items.quantity) DESC) AS rank
FROM stores
JOIN orders 
	ON stores.store_id = orders.store_id
JOIN order_items  
	ON orders.order_id = order_items.order_id
JOIN products  
	ON order_items.product_id = products.product_id
GROUP BY stores.country, products.product_name
ORDER BY stores.country, rank;