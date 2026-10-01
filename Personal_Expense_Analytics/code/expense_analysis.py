
import pandas as pd
import matplotlib.pyplot as plt
import os

# Project paths
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(base_path, "dataset", "expenses.csv")
output_path = os.path.join(base_path, "outputs")

os.makedirs(output_path, exist_ok=True)

# Load dataset
df = pd.read_csv(dataset_path)

# Data cleaning
df["Date"] = pd.to_datetime(df["Date"])
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Extract month
df["Month"] = df["Date"].dt.strftime("%B")

# Basic analysis
total_expense = df["Amount"].sum()
average_expense = df["Amount"].mean()

category_expense = df.groupby("Category")["Amount"].sum()
monthly_expense = df.groupby("Month")["Amount"].sum()

print("PERSONAL EXPENSE ANALYTICS")
print("--------------------------")

print("Total Expense: ₹", total_expense)
print("Average Expense: ₹", round(average_expense, 2))

print("\nCategory-wise Expenses:")
print(category_expense)

print("\nMonthly Expenses:")
print(monthly_expense)

# Category-wise bar chart
plt.figure(figsize=(9, 5))
category_expense.plot(kind="bar")
plt.title("Category-wise Expense Analysis")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_path, "category_expenses.png"))
plt.close()

# Monthly expense chart
monthly_order = ["January", "February", "March", "April"]
monthly_expense = monthly_expense.reindex(monthly_order, fill_value=0)

plt.figure(figsize=(9, 5))
monthly_expense.plot(kind="line", marker="o")
plt.title("Monthly Expense Analysis")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.tight_layout()
plt.savefig(os.path.join(output_path, "monthly_expenses.png"))
plt.close()

# Payment mode analysis
payment_expense = df.groupby("Payment_Mode")["Amount"].sum()

plt.figure(figsize=(7, 7))
payment_expense.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Mode Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(output_path, "payment_modes.png"))
plt.close()

# Save cleaned dataset
df.to_csv(os.path.join(output_path, "cleaned_expenses.csv"), index=False)

print("\nAnalysis completed successfully!")
print("Graphs saved in outputs folder.")