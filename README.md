# ☕ Coffee Shop Sales Analysis — 2025

A full end-to-end data analysis project for a fictional coffee shop chain running **15 stores across 5 countries** — Poland, the United Kingdom, Germany, France, and Spain. This project walks through the entire data workflow: from raw data and database design, through SQL analysis and Python visualizations, all the way to exportable chart assets ready for reporting.


## Project Structure

```
coffee-sales-analysis/
├── README.md                  
├── requirements.txt           
├── findings.md                
├── visualizations.py          
├── ERD.png                    
├── sql/
│   ├── schema.sql             
│   ├── analysis.sql           
│   └── indexes.sql            
├── coffee_data/               
│   ├── stores.csv
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── products.csv
├── query_results/             
│   ├── daily_revenue.csv
│   ├── monthly_revenue.csv
│   ├── top_products.csv
│   ├── revenue_by_category.csv
│   ├── store_revenue_by_city.csv
│   ├── peak_ordering_hours.csv
│   ├── top_customers_by_value.csv
│   ├── avg_basket_size.csv
│   ├── seasonal_drink_performance.csv
│   ├── repeat_customer_rate.csv
│   ├── revenue_by_loyalty_tier.csv
│   ├── top_customers_by_activity.csv
│   ├── top_10_customers_by_value.csv
│   ├── monthly_revenue_by_city.csv
│   └── top_products_by_country.csv
└── charts/                    
```

---

## Project Overview

| Detail | Info |
|---|---|
| **Domain** | Retail / Food & Beverage |
| **Timeframe** | January 2025 – December 2025 |
| **Stores** | 15 stores across Poland, UK, Germany, France, and Spain |
| **Database** | PostgreSQL |
| **Tools** | Python, SQL, Plotly, Pandas |

---

## Workflow

The project follows a clean, realistic data pipeline:

```
Raw CSV Data  →  PostgreSQL (schema + indexing)  →  SQL Analysis  →  Export Results  →  Python Visualizations  →  Charts
```

Raw data lives in `coffee_data/`. It was loaded into PostgreSQL using the schema defined in `sql/schema.sql`. All analytical queries were written in `sql/analysis.sql`, and their results were exported to `query_results/`. The Python script `visualizations.py` reads from those exports and generates all charts saved to `charts/`.

---

## Database Design

The database is built around 5 tables:

- **stores** — store ID, city, country
- **customers** — customer ID, name, loyalty tier
- **orders** — order ID, store ID, customer ID, timestamp
- **order_items** — order ID, product ID, quantity
- **products** — product ID, name, category, price

Indexes were added on foreign keys and frequently filtered columns to optimize query performance. See `sql/indexes.sql` for details. The full entity relationship diagram is available as `ERD.png`.

---

## SQL Analysis

The `sql/analysis.sql` file contains **15 analytical queries** covering:

| # | Query |
|---|---|
| 1 | Daily revenue trend |
| 2 | Monthly revenue trend |
| 3 | Top 10 best-selling products |
| 4 | Revenue by product category |
| 5 | Store-level revenue ranking |
| 6 | Peak ordering hours |
| 7 | Customer lifetime value (top 20) |
| 8 | Average basket size |
| 9 | Seasonal drink performance (Pumpkin Spice Latte) |
| 10 | Repeat customer rate |
| 11 | Revenue by loyalty tier |
| 12 | Top 10 customers by number of orders |
| 13 | Top 10 customers by revenue |
| 14 | Store revenue by month |
| 15 | Top products by country |

---

## Python Visualizations

The `visualizations.py` script generates **14 charts** saved to the `charts/` folder. Every chart loads its data from `query_results/` — no hardcoded values anywhere in the script.

| # | Chart | Type |
|---|---|---|
| 1 | Daily Revenue Trend | Line |
| 2 | Monthly Revenue | Bar |
| 3 | Top 10 Best-Selling Products | Horizontal Bar |
| 4 | Revenue by Product Category | Horizontal Bar |
| 5 | Store Revenue by City | Horizontal Bar |
| 6 | Peak Ordering Hours | Bar |
| 7 | Top 20 Customers by Lifetime Value | Horizontal Bar |
| 8 | Seasonal Drink Performance | Line |
| 9 | Revenue by Loyalty Tier | Horizontal Bar |
| 10 | Top 10 Customers by Orders | Horizontal Bar |
| 11 | Top 10 Customers by Revenue | Horizontal Bar |
| 12 | Monthly Revenue by City | Line |
| 13 | Annual Total Revenue by City | Bar |
| 14 | Best-Selling Product per Country | Horizontal Bar |

---

## Key Findings

A full breakdown of insights is available in [`findings.md`](findings.md). Here's a quick summary:

- **Manchester** generated the highest annual revenue across all 15 stores
- **February** was consistently the weakest revenue month across every city
- **Beans** is the top revenue-generating product category by a significant margin
- **Bronze tier** customers drive the majority of total revenue due to volume
- **Peak ordering hours** fall consistently in the morning, typical for a coffee chain
- The **Pumpkin Spice Latte** showed clear seasonal demand patterns across the year
- Revenue across all 15 stores was remarkably stable with minimal variance between cities

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/hassan-akhter/coffee_shop_sales_analysis_2025.git
cd coffee_shop_sales_analysis_2025
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the visualizations**
```bash
python visualizations.py
```

All 14 charts will be saved automatically to the `charts/` folder.

> **Note:** If you want to recreate the database from scratch, load the files from `coffee_data/` into PostgreSQL and run `sql/schema.sql` followed by `sql/indexes.sql`. Then run the queries in `sql/analysis.sql` and export the results to `query_results/`.


## Tech Stack

- **PostgreSQL** — database design, querying, index optimization
- **Python 3** — data processing and visualization
- **Pandas** — data loading and aggregation
- **Plotly Express** — interactive chart generation
- **Kaleido** — static PNG export from Plotly

## Author

**Hassan Akhter**

[GitHub](https://github.com/hassan-akhter) 

[LinkedIn](https://www.linkedin.com/in/hassanakhter122/)


## License

This project is for portfolio and educational purposes. All data is fictional and generated specifically for this analysis.
