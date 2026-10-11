# 🛒 Ecommerce Data Cleaning and Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-green)
![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-6BAED6)
![Project](https://img.shields.io/badge/Project-Data%20Analytics-orange)

## 📌 Project Overview

This project focuses on cleaning, preparing, and exploring an ecommerce dataset using Python.

The project includes data quality checks, missing-value analysis, duplicate detection, descriptive statistics, outlier analysis, correlation analysis, and visualizations to understand sales performance and customer order patterns.

The objective is to transform raw ecommerce data into a clean, structured, and analysis-ready dataset and communicate useful insights through charts and a comprehensive report.

## 🎯 Project Objectives

- Understand the structure of the ecommerce dataset.
- Inspect data types and identify data quality issues.
- Identify and review missing values.
- Check for duplicate records.
- Prepare a cleaned dataset for further analysis.
- Perform exploratory data analysis (EDA).
- Analyze monthly sales trends.
- Compare sales across product categories.
- Examine order status and payment methods.
- Analyze sales by referral source.
- Study relationships between numerical variables.
- Identify potential outliers.
- Create charts and a final project report.

## 🧰 Tools and Technologies

The project uses the following tools and technologies:

| Tool / Technology | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Excel | Dataset storage and inspection |
| CSV | Storage of cleaned data and reports |
| Visual Studio Code | Python development environment |
| GitHub | Project version control and portfolio |

## 📂 Project Files

The repository contains the following project files:

| File Name | Description |
|---|---|
| `Cleaned_Data.py` | Python script for data cleaning |
| `EDA_Analysis.py` | Python script for exploratory data analysis |
| `Dataset for Data Analytics .xlsx` | Original Excel dataset |
| `Cleaned_Dataset.csv` | Cleaned dataset in CSV format |
| `Cleaned_Dataset.xlsx` | Cleaned dataset in Excel format |
| `monthly_sales_trend.png` | Monthly sales trend visualization |
| `product_wise_sales.png` | Product-wise sales comparison |
| `order_status_analysis.png` | Analysis of order statuses |
| `payment_method_analysis.png` | Analysis of payment methods |
| `referral_source_sales.png` | Sales comparison by referral source |
| `correlation_heatmap.png` | Correlation between numerical variables |
| `boxplot_Quantity.png` | Outlier analysis for quantity |
| `boxplot_UnitPrice.png` | Outlier analysis for unit price |
| `boxplot_ItemsInCart.png` | Outlier analysis for items in cart |
| `boxplot_TotalPrice.png` | Outlier analysis for total price |
| `final_data_quality_report.csv` | Summary of data quality checks |
| `outlier_summary.csv` | Summary of potential outliers |
| `total_price_outlier_records.csv` | Records flagged for high total-price values |
| `Requirement.txt` | Project dependency information |
| `EDA_Report.docx` | Comprehensive EDA report with graphs |

**Note:** File names and locations above reflect the files prepared for this project. If you upload the files into separate folders, update the paths accordingly.

## 📊 Dataset Overview

The ecommerce dataset used in this project contains **1,200 records and 14 columns**.

The dataset includes order information, product details, pricing information, customer references, payment methods, order statuses, and referral sources.

### Main Dataset Columns

| Column Name | Description |
|---|---|
| `OrderID` | Unique order reference |
| `Date` | Date associated with the order |
| `CustomerID` | Customer reference |
| `Product` | Product category |
| `Quantity` | Number of units recorded |
| `UnitPrice` | Price per unit |
| `TotalPrice` | Total price recorded for the order |
| `ItemsInCart` | Number of items in the cart |
| `PaymentMethod` | Payment method used |
| `OrderStatus` | Current or recorded order status |
| `CouponCode` | Coupon code associated with the order |
| `ReferralSource` | Source through which the customer arrived |

The workbook contains 14 columns. The table above lists the principal fields used in the analysis; consult the source workbook for the complete column list.

## 🧹 Data Cleaning Process

The data cleaning process focuses on checking and improving data quality before performing analysis.

### 1. Data Inspection

- Loaded the original dataset.
- Examined the dataset structure.
- Checked column names and data types.
- Reviewed the number of rows and columns.
- Inspected sample records.

### 2. Missing-Value Analysis

- Checked columns for missing values.
- Reviewed the distribution of missing data.
- Examined missing values before deciding how to handle them.
- Prepared a data quality report.

Missing values should be handled according to the meaning of each column. Blank values should not automatically be replaced with zero.

### 3. Duplicate Detection

- Checked for completely duplicated records.
- Reviewed duplicate counts.
- Avoided removing records solely because individual values were repeated.

### 4. Data Type Validation

- Checked date fields.
- Reviewed numeric columns.
- Examined categorical variables.
- Prepared fields for analysis where necessary.

### 5. Outlier Analysis

Potential outliers were reviewed using boxplots and the Interquartile Range (IQR) method.

The supplied outlier summary flags:

- 8 potential outliers in `TotalPrice`.
- No outliers in `Quantity`.
- No outliers in `UnitPrice`.
- No outliers in `ItemsInCart`.

An outlier is not necessarily an error. Records should be investigated before being removed or modified.

### 6. Exporting the Cleaned Dataset

The cleaned data was exported into two formats:

- CSV
- Excel

These formats make the prepared data convenient to reuse in Python, Excel, Power BI, SQL workflows, and other analytical tools.

## 📈 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset and identify patterns.

### 1. Monthly Sales Trend

The monthly sales trend examines changes in total sales over time.

The analysis covers January 2023 to June 2025.

**Key finding:** June 2024 recorded the highest monthly `TotalPrice` at 68,068.54, while April 2023 recorded the lowest at 27,751.71.

The trend can help identify fluctuations that may warrant further investigation into seasonality, promotions, product mix, and order composition.

### 2. Product-Wise Sales Analysis

Product-wise sales analysis compares the total sales recorded for different products.

The chart helps identify products with higher and lower sales totals.

**Business application:**
- Review product-level sales performance.
- Support inventory planning.
- Identify products for further marketing analysis.
- Investigate changes in product demand.

### 3. Order Status Analysis

Order status analysis compares the number of records in each order-status category.

The dataset includes categories such as:

- Delivered
- Shipped
- Pending
- Cancelled
- Returned

This analysis can support further investigation into order fulfillment and customer experience.

### 4. Payment Method Analysis

Payment method analysis compares the distribution of orders across payment methods.

The dataset includes payment categories such as:

- Online
- Cash
- Credit Card
- Debit Card
- Gift Card

This analysis helps describe the payment methods recorded in the dataset.

### 5. Referral Source Sales Analysis

Referral source analysis compares recorded sales across customer acquisition sources.

The dataset includes sources such as:

- Instagram
- Email
- Google
- Facebook
- Referral

The comparison can help identify which sources are associated with higher recorded sales. It does not, by itself, establish marketing profitability or conversion rates.

### 6. Correlation Analysis

A correlation heatmap was created to examine relationships between numerical variables.

The supplied heatmap indicates the following positive correlations:

| Variable Pair | Correlation |
|---|---:|
| `UnitPrice` and `TotalPrice` | 0.72 |
| `Quantity` and `TotalPrice` | 0.62 |
| `Quantity` and `ItemsInCart` | 0.65 |

Correlation describes the strength and direction of a relationship. It does not establish that one variable causes changes in another.

### 7. Outlier Visualization

Boxplots were created for:

- `Quantity`
- `UnitPrice`
- `ItemsInCart`
- `TotalPrice`

These visualizations help identify observations that fall outside the typical range of the data.

Potential outliers should be investigated using the original order details before deciding whether any correction is necessary.

## 📉 Visualizations

The project includes the following visualizations:

| No. | Visualization | Purpose |
|---:|---|---|
| 1 | Monthly Sales Trend | Examine sales changes over time |
| 2 | Product-Wise Sales | Compare sales across products |
| 3 | Order Status Analysis | Compare order-status counts |
| 4 | Payment Method Analysis | Compare payment-method counts |
| 5 | Referral Source Sales | Compare sales across referral sources |
| 6 | Correlation Heatmap | Examine numerical relationships |
| 7 | Quantity Boxplot | Inspect quantity outliers |
| 8 | Unit Price Boxplot | Inspect unit-price outliers |
| 9 | Items in Cart Boxplot | Inspect cart-size outliers |
| 10 | Total Price Boxplot | Inspect total-price outliers |

## 🔍 Key Findings

The analysis produced the following findings:

1. The dataset contains 1,200 records and 14 columns.
2. The supplied data quality report records 309 missing cells.
3. The supplied report records zero completely duplicated rows.
4. Eight potential outliers were flagged in `TotalPrice`.
5. June 2024 had the highest monthly sales total in the analyzed period.
6. April 2023 had the lowest monthly sales total in the analyzed period.
7. `UnitPrice` and `TotalPrice` show a positive correlation of 0.72.
8. `Quantity` and `TotalPrice` show a positive correlation of 0.62.
9. Product, payment, order-status, and referral-source charts provide different views of recorded ecommerce activity.

These findings describe the supplied dataset and should not be interpreted as independently verified business results.

## 💡 Business Recommendations

Based on the analysis, the following actions may be useful:

- Investigate monthly sales fluctuations.
- Review high-sales and low-sales products.
- Examine cancellation and return patterns.
- Review missing values in important analytical fields.
- Investigate potential high-value orders before treating them as errors.
- Compare sales performance across referral sources.
- Examine the relationship between quantity, unit price, and total price.
- Track monthly sales using a consistent reporting process.
- Validate key findings against business rules and source records.

## ⚙️ How to Run the Project

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Download the Repository

Download or clone this repository to your computer.

### Step 3: Open the Project

Open the project folder in Visual Studio Code.

### Step 4: Install Dependencies

Open the terminal in the project environment and install the packages listed in `Requirement.txt`.

If your dependency file is named `requirements.txt` instead, use that exact filename.

### Step 5: Run the Data Cleaning Script

Run the following command from the project folder:

```bash
python Cleaned_Data.py
```

### Step 6: Run the EDA Script

Run the analysis script:

```bash
python EDA_Analysis.py
```

**Important:** These commands assume the scripts are in the current directory and that their input/output paths are configured correctly. If the scripts are inside another folder, or the dataset path differs, adjust the commands or paths accordingly.

## 📁 Suggested Repository Structure

For a clean and professional GitHub repository, the project can be organized as follows:

```text
Ecommerce-Data-Cleaning-EDA/
│
├── README.md
├── Cleaned_Data.py
├── EDA_Analysis.py
├── Requirement.txt
│
├── Data/
│   ├── Cleaned_Dataset.csv
│   └── Cleaned_Dataset.xlsx
│
├── Charts/
│   ├── monthly_sales_trend.png
│   ├── product_wise_sales.png
│   ├── order_status_analysis.png
│   ├── payment_method_analysis.png
│   ├── referral_source_sales.png
│   ├── correlation_heatmap.png
│   ├── boxplot_Quantity.png
│   ├── boxplot_UnitPrice.png
│   ├── boxplot_ItemsInCart.png
│   └── boxplot_TotalPrice.png
│
├── Reports/
│   ├── EDA_Report.docx
│   ├── final_data_quality_report.csv
│   ├── outlier_summary.csv
│   └── total_price_outlier_records.csv
│
└── Dataset for Data Analytics .xlsx
```

This is a suggested structure. Your current GitHub repository may have all files in its root directory; the paths in this README should match the structure you actually upload.

## 🚀 Future Improvements

Potential future enhancements include:

- Building an interactive Power BI dashboard.
- Performing deeper product-level analysis.
- Calculating cancellation and return rates.
- Comparing sales by month, quarter, and year.
- Investigating missing-value patterns.
- Creating reusable data quality checks.
- Developing a sales forecasting model.
- Adding automated tests for data validation.

## 📚 Project Deliverables

The project deliverables include:

- Python data cleaning script.
- Python EDA script.
- Original dataset.
- Cleaned dataset in CSV and Excel formats.
- Data quality report.
- Outlier summary and flagged records.
- Ten EDA visualizations.
- Comprehensive Word report.

## 🏁 Conclusion

This project demonstrates a practical workflow for ecommerce data cleaning and exploratory data analysis using Python.

It combines data quality checks, data preparation, descriptive analysis, visualizations, correlation analysis, and outlier review to make the dataset more useful for further analytical work.

The results provide a starting point for understanding sales patterns and recorded ecommerce activity. Additional validation and business context would be required before making operational or strategic decisions.

## 👤 Author

**Ankit Kumar**

Data Analytics | Python | Pandas | Excel | Exploratory Data Analysis

## 🔗 Connect

- GitHub: [Explore my GitHub profile](https://github.com/somenju)

---

⭐ If you find this project useful, consider giving the repository a star.
