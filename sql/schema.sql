-- COFFEE SALES DATABASE SCHEMA
-- Year: 2025
-- Stores: 15
-- Customers: ~60,000
-- Orders: ~250,000
-- Order Items: ~700,000

-- Drop tables if they already exist
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS stores;

-- STORES TABLE
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    city  VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);

-- PRODUCTS TABLE
CREATE TABLE products (
    product_id  INT PRIMARY KEY,
    product_name  VARCHAR(150) NOT NULL,
    category     VARCHAR(50) NOT NULL,
    price     NUMERIC(6,2) NOT NULL CHECK (price >= 0)
);

-- CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id  INT PRIMARY KEY,
    name     VARCHAR(150) NOT NULL,
    email       VARCHAR(200) NOT NULL,
    loyalty_tier  VARCHAR(20) CHECK (loyalty_tier IN ('Bronze', 'Silver', 'Gold')),
    signup_date  DATE NOT NULL
);

-- ORDERS TABLE
CREATE TABLE orders (
    order_id        INT PRIMARY KEY,
    customer_id     INT NOT NULL,
    store_id        INT NOT NULL,
    order_timestamp TIMESTAMP NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),

    CONSTRAINT fk_orders_store
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
);


-- ORDER ITEMS TYABLE
CREATE TABLE order_items (
    order_item_id   INT PRIMARY KEY,
    order_id        INT NOT NULL,
    product_id      INT NOT NULL,
    quantity        INT NOT NULL CHECK (quantity > 0),

    CONSTRAINT fk_items_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id),

    CONSTRAINT fk_items_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_customers_loyalty_tier ON customers(loyalty_tier);
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_orders_timestamp ON orders(order_timestamp);
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_store_id ON orders(store_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_stores_city ON stores(city);
CREATE INDEX idx_stores_country ON stores(country);