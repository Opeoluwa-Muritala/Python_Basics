"""
09 - Data Analytics with pandas / numpy / matplotlib
------------------------------------------------------
A walkthrough of a typical data analysis workflow:
load data -> inspect -> clean -> transform -> aggregate -> visualize -> export.

This script generates its own sample dataset (loan applications for a
microfinance bank) so it runs standalone with no external files needed.

Install requirements if missing:
    pip install pandas numpy matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. CREATE / LOAD DATA
# ----------------------------------------------------------------------
# In real projects you'd normally load data like this instead:
#   df = pd.read_csv("loans.csv")
#   df = pd.read_excel("loans.xlsx")
#   df = pd.read_sql("SELECT * FROM loans", connection)

np.random.seed(42)  # makes the random data reproducible

n = 200  # number of rows to simulate

branches = ["Ikeja", "Lekki", "Yaba", "Ajah", "Surulere"]
statuses = ["Approved", "Rejected", "Pending"]

df = pd.DataFrame({
    "application_id": range(1001, 1001 + n),
    "branch": np.random.choice(branches, size=n),
    "loan_amount": np.random.randint(50_000, 2_000_000, size=n).astype(float),
    "interest_rate": np.round(np.random.uniform(2.0, 8.0, size=n), 2),
    "status": np.random.choice(statuses, size=n, p=[0.6, 0.25, 0.15]),
    "applicant_age": np.random.randint(21, 65, size=n),
    "application_date": pd.date_range("2026-01-01", periods=n, freq="D"),
})

# Deliberately introduce some missing values and a duplicate row,
# to mimic real, messy data
df.loc[5:8, "interest_rate"] = np.nan
df.loc[15, "loan_amount"] = np.nan
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)  # duplicate row 0

print("=" * 60)
print("1. RAW DATA PREVIEW")
print("=" * 60)
print(df.head())          # first 5 rows
print("\nShape (rows, cols):", df.shape)


# ----------------------------------------------------------------------
# 2. INSPECT DATA
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("2. INSPECTING THE DATA")
print("=" * 60)

print("\n-- Data types --")
print(df.dtypes)

print("\n-- Summary statistics (numeric columns) --")
print(df.describe())

print("\n-- Missing values per column --")
print(df.isna().sum())

print("\n-- Duplicate rows --")
print("Duplicate count:", df.duplicated().sum())


# ----------------------------------------------------------------------
# 3. CLEAN DATA
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("3. CLEANING")
print("=" * 60)

# Drop exact duplicate rows
df = df.drop_duplicates()

# Fill missing interest_rate with the column's median (robust to outliers)
median_rate = df["interest_rate"].median()
df["interest_rate"] = df["interest_rate"].fillna(median_rate)

# Fill missing loan_amount with the median loan amount for that branch
df["loan_amount"] = df.groupby("branch")["loan_amount"].transform(
    lambda x: x.fillna(x.median())
)

print("Missing values after cleaning:")
print(df.isna().sum())
print("Rows after removing duplicates:", len(df))


# ----------------------------------------------------------------------
# 4. TRANSFORM / FEATURE ENGINEERING
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("4. TRANSFORMING DATA")
print("=" * 60)

# Create a new column using a condition (vectorized, no loop needed)
df["amount_tier"] = pd.cut(
    df["loan_amount"],
    bins=[0, 250_000, 1_000_000, np.inf],
    labels=["Small", "Medium", "Large"],
)

# Extract the month from the date column for time-based analysis
df["month"] = df["application_date"].dt.month_name()

# Boolean/filter-based column
df["is_approved"] = df["status"] == "Approved"

print(df[["application_id", "loan_amount", "amount_tier", "month", "is_approved"]].head())


# ----------------------------------------------------------------------
# 5. FILTER & SELECT
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("5. FILTERING")
print("=" * 60)

# Boolean indexing: rows where a condition is True
approved_large_loans = df[(df["status"] == "Approved") & (df["amount_tier"] == "Large")]
print(f"Approved large loans: {len(approved_large_loans)} rows")

# .loc for label-based selection of specific rows/columns
lekki_data = df.loc[df["branch"] == "Lekki", ["application_id", "loan_amount", "status"]]
print("\nLekki branch sample:")
print(lekki_data.head())


# ----------------------------------------------------------------------
# 6. GROUP BY & AGGREGATE
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("6. GROUPING & AGGREGATION")
print("=" * 60)

# Average loan amount and approval rate per branch
branch_summary = df.groupby("branch").agg(
    total_applications=("application_id", "count"),
    avg_loan_amount=("loan_amount", "mean"),
    avg_interest_rate=("interest_rate", "mean"),
    approval_rate=("is_approved", "mean"),  # mean of booleans = proportion True
).round(2)

branch_summary = branch_summary.sort_values("avg_loan_amount", ascending=False)
print(branch_summary)

# Cross-tab: counts of status per branch (like a pivot table)
status_by_branch = pd.crosstab(df["branch"], df["status"])
print("\nStatus counts by branch:")
print(status_by_branch)

# Pivot table: average loan amount by branch and status
pivot = df.pivot_table(
    values="loan_amount",
    index="branch",
    columns="status",
    aggfunc="mean",
).round(0)
print("\nAverage loan amount by branch & status:")
print(pivot)


# ----------------------------------------------------------------------
# 7. SORTING & RANKING
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("7. SORTING & TOP-N")
print("=" * 60)

top_5_loans = df.nlargest(5, "loan_amount")[["application_id", "branch", "loan_amount", "status"]]
print("Top 5 largest loans:")
print(top_5_loans)


# ----------------------------------------------------------------------
# 8. VISUALIZE
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("8. VISUALIZING (saving charts as PNG files)")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Bar chart: average loan amount per branch
branch_summary["avg_loan_amount"].plot(
    kind="bar", ax=axes[0, 0], color="#89268B", title="Avg Loan Amount by Branch"
)
axes[0, 0].set_ylabel("Naira")
axes[0, 0].tick_params(axis="x", rotation=45)

# Pie chart: application status breakdown
df["status"].value_counts().plot(
    kind="pie", ax=axes[0, 1], autopct="%1.0f%%", title="Application Status Breakdown"
)
axes[0, 1].set_ylabel("")

# Histogram: distribution of loan amounts
df["loan_amount"].plot(
    kind="hist", bins=20, ax=axes[1, 0], color="#2E0052", title="Loan Amount Distribution"
)
axes[1, 0].set_xlabel("Naira")

# Line chart: number of applications per month
monthly_counts = df.groupby("month").size().reindex([
    "January", "February", "March", "April", "May", "June", "July"
]).dropna()
monthly_counts.plot(kind="line", marker="o", ax=axes[1, 1], title="Applications Over Time")
axes[1, 1].set_ylabel("Applications")

plt.tight_layout()
plt.savefig("loan_analytics_dashboard.png", dpi=150)
print("Saved chart: loan_analytics_dashboard.png")
plt.close()


# ----------------------------------------------------------------------
# 9. EXPORT RESULTS
# ----------------------------------------------------------------------
print("\n" + "=" * 60)
print("9. EXPORTING RESULTS")
print("=" * 60)

# Export the cleaned dataset and the summary table
df.to_csv("cleaned_loans.csv", index=False)
branch_summary.to_csv("branch_summary.csv")

print("Saved: cleaned_loans.csv")
print("Saved: branch_summary.csv")

print("\nDone. Analysis complete.")
