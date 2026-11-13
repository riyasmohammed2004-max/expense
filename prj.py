import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
months = ["July", "August", "September"]
past_income = np.array([18000, 20000, 22000])
past_expenses = np.array([12000, 14000, 15000])
income = float(input("Enter this month's income: "))
print("\nEnter your expenses:")
food = float(input("Food: "))
travel = float(input("Travel: "))
rent = float(input("Rent: "))
shopping = float(input("Shopping: "))
other = float(input("Other expenses: "))
categories = ["Food", "Travel", "Rent", "Shopping", "Other"]
amounts = [food, travel, rent, shopping, other]
present_expense = sum(amounts)
present_saving = income - present_expense
past_average = np.mean(past_expenses)
future_expense = (
    past_average + present_expense) / 2
future_income = (
    np.mean(past_income) + income) / 2
future_saving = future_income - future_expense
print("\n--- PRESENT MONTH ---")
print("Income: Rs.", income)
print("Total Expenses: Rs.", present_expense)
print("Savings / Balance: Rs.", present_saving)
if present_saving > 0:
    print("Status: Saving / money left")
elif present_saving < 0:
    print("Status: Loss / money shortage")
else:
    print("Status: Break-even")
print("\n--- NEXT MONTH PREDICTION ---")
print("Expected Income: Rs.", round(future_income, 2))
print("Expected Expenses: Rs.", round(future_expense, 2))
print("Expected Savings: Rs.", round(future_saving, 2))
change = future_expense - present_expense
if change > 0:
    print("Expenses may increase by Rs.", round(change, 2))
elif change < 0:
    print("Expenses may decrease by Rs.", round(abs(change), 2))
else:
    print("Expenses may remain the same")
target_saving = future_income * 0.20
print("\n--- SAVINGS PLAN ---")
print("Target: Save 20% of income")
print("Target saving: Rs.", round(target_saving, 2))

if future_saving >= target_saving:
    print("Good! 👌❤️You can reach your savings target.")
elif future_saving > 0:
    print("Reduce expenses to reach your savings target😒🤦‍♂️.")
else:
    print("Warning! Expected expenses exceed income😯😔.")
all_months = months + ["October", "November (Predicted)"]
all_income = list(past_income) + [income, future_income]
all_expenses = list(past_expenses) + [present_expense, future_expense]
df = pd.DataFrame({
    "Month": all_months,
    "Income": all_income,
    "Expenses": all_expenses
})
df["Savings"] = df["Income"] - df["Expenses"]
print("\n--- MONTHLY TRACKER ---")
print(df.round(2).to_string(index=False))
plt.figure(figsize=(9, 5))
x = np.arange(len(all_months))
width = 0.35
plt.bar(x - width/2, all_income, width, label="Income")
plt.bar(x + width/2, all_expenses, width, label="Expenses")
plt.xticks(x, all_months, rotation=20)
plt.ylabel("Amount (Rs.)")
plt.title("Past, Present and Predicted Expenses")
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(9, 5))
plt.plot(all_months, df["Savings"], marker="o", label="Savings / Balance")
plt.axhline(y=0, linestyle="--")
plt.title("Monthly Savings Comparison")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=20)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(7, 5))
plt.bar(categories, amounts)
plt.title("Present Month Expense Categories")
plt.ylabel("Amount (Rs.)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()