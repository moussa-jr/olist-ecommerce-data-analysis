# 🛒 Olist E-Commerce Data Analysis & Market Insights

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Tech Stack](https://img.shields.io/badge/Tools-SQL%20%7C%20Excel%20%7C%20Python-blue)
![Python Version](https://img.shields.io/badge/Python-3.x-yellow)

An end-to-end data analysis project exploring the **Olist E-Commerce Dataset** from Brazil[cite: 2]. This project demonstrates a full data pipeline: extracting and querying relational databases using **SQL**, refining metrics and growth rates in **Excel**, and automating visualization workflows in **Python (Pandas & Matplotlib)**[cite: 2].

**Author:** Mohamed Moussa[cite: 2]  

---

## 📌 Project Overview & Pipeline
The goal of this analysis is to evaluate sales performance, identify key market hubs, analyze product demand in top regions, and provide strategic business recommendations[cite: 2].

┌────────────────┐     ┌────────────────┐     ┌─────────────────────┐
│   1. SQL       │ ──> │   2. Excel     │ ──> │   3. Python         │
│ Data Extraction│     │ Processing     │     │ Automated Plotting  │
└────────────────┘     └────────────────┘     └─────────────────────┘
---

## 🚀 Key Analysis Phases

### Phase 1: Monthly Sales Summary & Trends[cite: 2]
* **SQL:** Extracted order timestamps and prices from `olist_orders` and `order_items` tables, filtering for `delivered` status to calculate monthly revenue and order volume[cite: 2].
* **Excel:** Calculated Month-over-Month (MoM) growth rates and cleaned dataset[cite: 2].
* **Python:** Plotted a time-series line chart tracking sales trajectories from 2016 to 2018[cite: 2].
* **Key Insight:** Clear upward sales trend with significant revenue spikes in late 2017 corresponding to Brazilian retail holidays (e.g., Black Friday)[cite: 2].

---

### Phase 2: Top Cities Performance & Regional Dominance[cite: 2]
* **SQL:** Multi-table join across `Orders`, `Customers`, and `Items` to aggregate total revenue, order count, and Average Order Value (AOV) per city[cite: 2].
* **Excel:** Quantified market share percentage and order probabilities for the top 10 hubs[cite: 2].
* **Python:** Built a customized teal bar chart visualizing revenue distribution across cities[cite: 2].
* **Key Insight:** **Sao Paulo** is the primary market driver, generating over $1.9M in revenue (with top 2 cities accounting for over 40% of top-tier sales)[cite: 2].

---

### Phase 3: Sao Paulo Product Category Analysis[cite: 2]
* **SQL:** Joined 4 relational datasets (`Orders`, `Customers`, `Order_Items`, `Products`) to isolate delivered orders specifically in the Sao Paulo market[cite: 2].
* **Excel:** Mapped product categories and formatted high-density revenue contribution data[cite: 2].
* **Python:** Generated a horizontal bar chart (`barh`) with a salmon color scheme for clear category rankings[cite: 2].
* **Key Insight:** **Health & Beauty (`beleza_saude`)** and **Bed, Bath & Table (`cama_mesa_banho`)** are the highest-grossing product categories in Sao Paulo[cite: 2].

---

## 💡 Strategic Business Recommendations
1. **Logistics Optimization:** Prioritize fulfillment center placements and warehouse capacity in **Sao Paulo** to optimize shipping speeds and reduce costs[cite: 2].
2. **Targeted Campaigns:** Focus marketing budgets on high-demand lifestyle categories like **Personal Care/Health & Beauty** during Q4 peak seasons[cite: 2].
3. **Inventory Planning:** Use historical peak season insights to forecast stock requirements for holiday demand surges[cite: 2].

---

## 🛠️ Tech Stack & Libraries
* **Database Management:** SQL Server Management Studio (SSMS) / SQL[cite: 2]
* **Spreadsheet Processing:** Microsoft Excel (MoM %, Market Share calculations)[cite: 2]
* **Data Science & Visualization:** Python 3, Pandas, Matplotlib[cite: 2]
* **IDE:** PyCharm / VS Code[cite: 2]

---

## 📁 Repository Structure

├── sql_queries/       # SQL scripts for data extraction & joins
├── data/              # Refined CSV / Excel files
├── scripts/           # Python plotting & automation scripts (.py)
├── visuals/           # Generated charts & figures
└── README.md          # Project documentation
