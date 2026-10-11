import pandas as pd
from pathlib import Path

# Load cleaned dataset
df = pd.read_csv("C:\\INTERNSHIP_PY\\Week_2\\Cleaned_Output\\Cleaned_Dataset.csv")

# Descriptive statistics
print("\n===== DESCRIPTIVE STATISTICS =====")

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

print(df[numeric_columns].describe().round(2))

# Mean
print("\n===== MEAN =====")
print(df[numeric_columns].mean().round(2))

# Median
print("\n===== MEDIAN =====")
print(df[numeric_columns].median().round(2))

# Count
print("\n===== COUNT =====")
print(df[numeric_columns].count())



# ==========================================
# STEP 7: PRODUCT-WISE SALES ANALYSIS
# ==========================================

import matplotlib.pyplot as plt

# Calculate total sales for each product
product_sales = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT-WISE TOTAL SALES =====")
print(product_sales.round(2))

# Create bar chart
plt.figure(figsize=(10, 6))

product_sales.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)
output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "product_wise_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved in EDA_Charts folder.")


# ==========================================
# STEP 7: PRODUCT-WISE SALES ANALYSIS
# ==========================================

import matplotlib.pyplot as plt

# Calculate total sales for each product
product_sales = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT-WISE TOTAL SALES =====")
print(product_sales.round(2))

# Create bar chart
plt.figure(figsize=(10, 6))

product_sales.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)
output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "product_wise_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved in EDA_Charts folder.")



# ==========================================
# STEP 8: ORDER STATUS ANALYSIS
# ==========================================

import matplotlib.pyplot as plt

# Count orders by status
status_counts = df["OrderStatus"].value_counts()

print("\n===== ORDER STATUS COUNTS =====")
print(status_counts)

# Calculate percentages
status_percentages = (
    df["OrderStatus"].value_counts(normalize=True) * 100
).round(2)

print("\n===== ORDER STATUS PERCENTAGES =====")
print(status_percentages)

# Create bar chart
plt.figure(figsize=(9, 5))

status_counts.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Distribution of Order Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "order_status_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nOrder status chart saved successfully.")


# ==========================================
# STEP 9: PAYMENT METHOD ANALYSIS
# ==========================================

# Count orders by payment method
payment_counts = df["PaymentMethod"].value_counts()

print("\n===== PAYMENT METHOD COUNTS =====")
print(payment_counts)

# Calculate percentages
payment_percentages = (
    df["PaymentMethod"].value_counts(normalize=True) * 100
).round(2)

print("\n===== PAYMENT METHOD PERCENTAGES =====")
print(payment_percentages)

# Create chart
plt.figure(figsize=(9, 5))

payment_counts.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "payment_method_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nPayment method chart saved successfully.")




# ==========================================
# STEP 10: MONTHLY SALES TREND ANALYSIS
# ==========================================

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove rows without a valid date for this analysis
date_df = df.dropna(subset=["Date"]).copy()

# Group sales by month
date_df["Month"] = date_df["Date"].dt.to_period("M")

monthly_sales = (
    date_df.groupby("Month")["TotalPrice"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# Create line chart
plt.figure(figsize=(12, 6))

monthly_sales.index = monthly_sales.index.astype(str)

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()

# Save chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nMonthly sales chart saved successfully.")


# ==========================================
# STEP 11: REFERRAL SOURCE ANALYSIS
# ==========================================

# Count orders by referral source
referral_counts = df["ReferralSource"].value_counts()

print("\n===== ORDERS BY REFERRAL SOURCE =====")
print(referral_counts)

# Calculate sales by referral source
referral_sales = (
    df.groupby("ReferralSource")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOTAL SALES BY REFERRAL SOURCE =====")
print(referral_sales.round(2))

# Create sales chart
plt.figure(figsize=(10, 6))

referral_sales.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Total Sales by Referral Source")
plt.xlabel("Referral Source")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)
output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "referral_source_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nReferral source chart saved successfully.")




# ==========================================
# STEP 12: CORRELATION ANALYSIS
# ==========================================

import matplotlib.pyplot as plt

# Select numerical columns
numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

# Calculate correlation matrix
correlation_matrix = df[numeric_columns].corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix.round(2))

# Create correlation heatmap
plt.figure(figsize=(8, 6))

image = plt.imshow(
    correlation_matrix,
    vmin=-1,
    vmax=1,
    aspect="auto"
)

plt.colorbar(image, label="Correlation")

plt.xticks(
    range(len(numeric_columns)),
    numeric_columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(numeric_columns)),
    numeric_columns
)

# Display correlation values
for i in range(len(numeric_columns)):
    for j in range(len(numeric_columns)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")
plt.tight_layout()

# Save chart
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

output_folder.mkdir(exist_ok=True)

plt.savefig(
    output_folder / "correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCorrelation heatmap saved successfully.")



# ==========================================
# STEP 13: OUTLIER DETECTION USING IQR
# ==========================================

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

print("\n===== OUTLIER DETECTION =====")

outlier_summary = []

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    outlier_summary.append({
        "Column": column,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Lower_Bound": lower_bound,
        "Upper_Bound": upper_bound,
        "Outlier_Count": len(outliers)
    })

    print(f"\nColumn: {column}")
    print("Lower bound:", round(lower_bound, 2))
    print("Upper bound:", round(upper_bound, 2))
    print("Outlier count:", len(outliers))

outlier_report = pd.DataFrame(outlier_summary)

print("\n===== OUTLIER SUMMARY =====")
print(outlier_report.round(2).to_string(index=False))

# Save report
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)
output_folder.mkdir(exist_ok=True)

outlier_report.to_csv(
    output_folder / "outlier_summary.csv",
    index=False
)

print("\nOutlier report saved successfully.")



# ==========================================
# STEP 14: INSPECT TOTAL PRICE OUTLIERS
# ==========================================

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

total_price_outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print("\n===== TOTAL PRICE OUTLIER RECORDS =====")

columns_to_show = [
    "OrderID",
    "Product",
    "Quantity",
    "UnitPrice",
    "TotalPrice",
    "OrderStatus"
]

print(
    total_price_outliers[columns_to_show].to_string(index=False)
)

# Save outlier records for review
output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

total_price_outliers[columns_to_show].to_csv(
    output_folder / "total_price_outlier_records.csv",
    index=False
)

print("\nOutlier records saved successfully.")



# ==========================================
# STEP 15: BOXPLOT FOR OUTLIER VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt
from pathlib import Path

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

output_folder = (
    Path(__file__).resolve().parent / "EDA_Charts"
)

output_folder.mkdir(exist_ok=True)

for column in numeric_columns:

    plt.figure(figsize=(9, 5))

    plt.boxplot(
        df[column].dropna(),
        vert=False
    )

    plt.title(f"Box Plot of {column}")
    plt.xlabel(column)
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()

    chart_path = output_folder / f"boxplot_{column}.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Saved: {chart_path.name}")

print("\nAll box plots created successfully.")


# ==========================================
# STEP 16: FINAL DATA QUALITY REPORT
# ==========================================

import pandas as pd
from pathlib import Path

# Load the cleaned dataset
base_folder = Path(__file__).resolve().parent

df = pd.read_csv(
    base_folder / "Cleaned_Dataset.csv"
)

# Create a data quality summary
quality_report = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Duplicate Rows",
        "Total Missing Values",
        "Columns With Missing Values",
        "Numerical Columns",
        "Categorical Columns"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.duplicated().sum()),
        int(df.isnull().sum().sum()),
        int((df.isnull().sum() > 0).sum()),
        len(df.select_dtypes(include="number").columns),
        len(df.select_dtypes(include="object").columns)
    ]
})

# Display report
print("\n===== FINAL DATA QUALITY REPORT =====")
print(quality_report.to_string(index=False))

# Save report
output_folder = base_folder / "EDA_Charts"
output_folder.mkdir(exist_ok=True)

quality_report.to_csv(
    output_folder / "final_data_quality_report.csv",
    index=False
)

print("\nFinal data quality report saved successfully.")
