import pandas as pd
# ==========================================
# DATA ANALYTICS PROJECT 2
# STEP 1: LOAD AND INSPECT DATASET
# ==========================================
 

# Load the Excel dataset

df = pd.read_excel(r"C:\INTERNSHIP_PY\Week_2\Dataset for Data Analytics .xlsx")








# Display first five rows
print("\nFIRST FIVE ROWS")
print(df.head())

# Display dataset dimensions
print("\nDATASET SHAPE")
print("Rows and columns:", df.shape)

# Display column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Display column data types
print("\nDATA TYPES")
print(df.dtypes)

# Display dataset information
print("\nDATASET INFORMATION")
df.info()

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check completely duplicated rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())




# ==========================================
# STEP 2: MISSING VALUE ANALYSIS
# ==========================================

print("\nMISSING VALUE ANALYSIS")

missing_count = df.isnull().sum()

missing_percentage = (
    df.isnull().sum() / len(df) * 100
).round(2)

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage
})

print(missing_report[missing_report["Missing_Count"] > 0])


# ==========================================
# STEP 3: INVESTIGATE COUPON CODES
# ==========================================

print("\nCOUPON CODE COUNTS")

print(df["CouponCode"].value_counts(dropna=False))

print("\nSAMPLE ROWS WITH MISSING COUPON CODES")

print(
    df[df["CouponCode"].isnull()]
    [["OrderID", "Product", "TotalPrice", "CouponCode"]]
    .head(10)
)


# ==========================================
# STEP 4: CHECK DUPLICATE ORDER IDs
# ==========================================

print("\nDUPLICATE ORDER ID ANALYSIS")

print("Total duplicate OrderIDs:",
      df["OrderID"].duplicated().sum())

# Display duplicate OrderIDs
duplicate_orders = df[
    df["OrderID"].duplicated(keep=False)
].sort_values("OrderID")

print("\nDuplicate OrderID Records:")
print(duplicate_orders)



# ==========================================
# STEP 5: CHECK DATA TYPES
# ==========================================

print("\nDATA TYPES BEFORE CLEANING")

print(df.dtypes)

# Check date column
print("\nDATE COLUMN SAMPLE")
print(df["Date"].head())

# Check numerical columns
print("\nNUMERICAL DATA SUMMARY")

print(
    df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]]
    .describe()
)


# ==========================================
# STEP 6: CHECK CATEGORICAL VALUES
# ==========================================

categorical_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "CouponCode",
    "ReferralSource"
]

for column in categorical_columns:

    print(f"\nUNIQUE VALUES IN {column}")

    print(df[column].value_counts(dropna=False))
    
    # ==========================================
# STEP 7: DATA TYPE CHECKING AND CONVERSION
# ==========================================

print("\n--- DATA TYPES BEFORE CLEANING ---")
print(df.dtypes)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Convert numerical columns to numeric format
numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

print("\n--- DATA TYPES AFTER CLEANING ---")
print(df.dtypes)

# Check invalid dates
print("\nInvalid or missing dates:", df["Date"].isna().sum())

# Check missing numerical values
print("\nMissing values in numerical columns:")
print(df[numeric_columns].isna().sum())


# ==========================================
# STEP 8: CHECK INVALID NUMERICAL VALUES
# ==========================================

print("\n--- QUANTITY LESS THAN OR EQUAL TO ZERO ---")

print(
    df[df["Quantity"] <= 0][
        ["OrderID", "Product", "Quantity", "UnitPrice", "TotalPrice"]
    ]
)

print("\n--- UNIT PRICE LESS THAN ZERO ---")

print(
    df[df["UnitPrice"] < 0][
        ["OrderID", "Product", "UnitPrice", "TotalPrice"]
    ]
)

print("\n--- TOTAL PRICE LESS THAN ZERO ---")

print(
    df[df["TotalPrice"] < 0][
        ["OrderID", "Product", "TotalPrice"]
    ]
)




# ==========================================
# STEP 9: TOTAL PRICE VALIDATION
# ==========================================

df["ExpectedTotalPrice"] = (
    df["Quantity"] * df["UnitPrice"]
)

df["PriceDifference"] = (
    df["TotalPrice"] - df["ExpectedTotalPrice"]
).round(2)

price_mismatches = df[
    df["PriceDifference"].abs() > 0.01
]

print("\n--- TOTAL PRICE MISMATCHES ---")

print("Number of mismatches:", len(price_mismatches))

print(
    price_mismatches[
        [
            "OrderID",
            "Quantity",
            "UnitPrice",
            "TotalPrice",
            "ExpectedTotalPrice",
            "PriceDifference"
        ]
    ]
)

# ==========================================
# STEP 13: EXPORT CLEANED DATASET
# ==========================================

from pathlib import Path

# Create output folder
output_folder = Path(__file__).resolve().parent / "Cleaned_Output"
output_folder.mkdir(exist_ok=True)

# Remove temporary validation columns
df_export = df.drop(
    columns=["ExpectedTotalPrice", "PriceDifference"],
    errors="ignore"
)

# Save cleaned dataset as Excel
excel_path = output_folder / "Cleaned_Dataset.xlsx"
df_export.to_excel(excel_path, index=False)

# Save cleaned dataset as CSV
csv_path = output_folder / "Cleaned_Dataset.csv"
df_export.to_csv(csv_path, index=False)

print("\n--- DATASET EXPORTED SUCCESSFULLY ---")
print("Excel file:", excel_path)
print("CSV file:", csv_path)
print("Final rows:", df_export.shape[0])
print("Final columns:", df_export.shape[1])
print("Remaining missing values:")
print(df_export.isnull().sum())

# ==========================================
# STEP 14: STANDARDIZE TEXT COLUMNS
# ==========================================

text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "CouponCode",
    "ReferralSource"
]

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )

print("\nTEXT CLEANING COMPLETED")

for column in text_columns:
    print(f"{column}: {df[column].nunique()} unique values")


# ==========================================
# STEP 15: FINAL DATA QUALITY CHECK
# ==========================================

print("\n--- FINAL DATA QUALITY REPORT ---")

print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Completely duplicated rows:", df.duplicated().sum())

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nTotal price mismatches:")

expected_total = df["Quantity"] * df["UnitPrice"]

mismatches = (
    (df["TotalPrice"] - expected_total).abs() > 0.01
).sum()

print(mismatches)


# ==========================================
# STEP 19: EXPORT FINAL CLEANED DATASET
# ==========================================

from pathlib import Path

# Create output folder
output_folder = Path(__file__).resolve().parent / "Cleaned_Output"
output_folder.mkdir(exist_ok=True)

# Remove temporary validation columns
df_export = df.drop(
    columns=["ExpectedTotalPrice", "PriceDifference"],
    errors="ignore"
)

# Save Excel file
df_export.to_excel(
    output_folder / "Cleaned_Dataset.xlsx",
    index=False
)

# Save CSV file
df_export.to_csv(
    output_folder / "Cleaned_Dataset.csv",
    index=False
)

# Final report
print("\n===== FINAL EXPORT REPORT =====")
print("Rows:", df_export.shape[0])
print("Columns:", df_export.shape[1])
print("Duplicate rows:", df_export.duplicated().sum())
print("\nMissing values:")
print(df_export.isnull().sum())

print("\nBoth files saved successfully!")

