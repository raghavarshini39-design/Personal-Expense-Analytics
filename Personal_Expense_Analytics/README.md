# Personal Expense Analytics

**Intern ID:** CITS8924  
**Organization:** CODTECH IT SOLUTIONS  
**Internship Duration:** 6 Weeks

## Project Overview

Personal Expense Analytics is a Python-based data analysis project that helps users understand their spending patterns. It analyzes personal expenses using different categories, monthly expenses, and payment modes.

## Objectives

* Analyze personal spending habits.
* Calculate total and average expenses.
* Identify expenses based on categories.
* Analyze monthly spending patterns.
* Visualize payment mode distribution.
* Generate graphs for better understanding.

## Technologies Used

* Python
* Pandas
* Matplotlib
* CSV Dataset
* Visual Studio Code

## Project Documentation

The complete project report is available in PDF format.

[View Personal Expense Analytics Project Report](Personal_Expense_Analytics.pdf)

The report includes the project objectives, scope, dataset description, methodology, Python implementation, analysis, visualizations, results, and conclusion.

## Project Structure

```text
Personal_Expense_Analytics/
│
├── code/
│   └── expense_analysis.py
│
├── dataset/
│   └── expenses.csv
│
├── outputs/
│   ├── category_expenses.png
│   ├── monthly_expenses.png
│   ├── payment_modes.png
│   └── cleaned_expenses.csv
│
├── screenshots/
├── Personal_Expense_Analytics.pdf
│
└── README.md
```

## Dataset Description

The dataset contains personal expense information with the following attributes:

* Date
* Category
* Description
* Amount
* Payment Mode

## Analysis Performed

### 1. Total and Average Expense

Calculated the total amount spent and the average expense per transaction.

### 2. Category-wise Expense Analysis

Analyzed expenses across different categories such as Education, Entertainment, Food, Shopping, and Transport.

### 3. Monthly Expense Analysis

Compared expenses across January, February, March, and April.

### 4. Payment Mode Analysis

Analyzed expenses based on payment methods such as UPI, Cash, and Card.

## Results

* Total Expense: ₹13,530
* Average Expense: ₹676.50
* Highest Spending Category: Shopping
* Highest Spending Month: February
* Most Used Payment Mode by Amount: Card

## Output Files

The project generates the following output files:

* `category_expenses.png` – Category-wise expense bar chart.
* `monthly_expenses.png` – Monthly expense line chart.
* `payment_modes.png` – Payment mode pie chart.
* `cleaned_expenses.csv` – Cleaned dataset.

## How to Run the Project

1. Install Python.
2. Install required libraries:

```bash
pip install pandas matplotlib
```

3. Open the project folder in VS Code.
4. Run the Python file:

```bash
python code/expense_analysis.py
```

## Conclusion

The Personal Expense Analytics project successfully analyzes personal spending data using Python. It provides useful insights into spending categories, monthly expenses, and payment methods through graphical visualizations.
