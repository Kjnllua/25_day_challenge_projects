import matplotlib.pyplot as plt

# Main data
monthly_income: float = 8500
rent: float = 1000
food: float = 2500
taxes: float = monthly_income * 0.10
other_expenses: float = 2000

# Yearly
yearly_income: float = monthly_income * 12
yearly_expenses: float = sum([rent, food, taxes, other_expenses]) * 12
yearly_savings: float = yearly_income - yearly_expenses

# Prepare data for plotting
monthly_categories = ['Income', 'Rent', 'Food', 'Taxes', 'Other']
monthly_amounts = [monthly_income, rent, food, taxes, other_expenses]
monthly_colors = ['green', 'red', 'red', 'red', 'red']

yearly_categories = ['Income', 'Expenses', 'Savings']
yearly_amounts = [yearly_income, yearly_expenses, yearly_savings]
yearly_colors = ['green', 'red', 'green']

# Create subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(10, 6))

# Monthly bar chart
axs[0].bar(monthly_categories, monthly_amounts, color=monthly_colors)
axs[0].set_title('Monthly Financial Overview')
axs[0].set_ylabel('Amount ($)')
axs[0].tick_params(axis='x', rotation=45)

# Yearly bar chart
axs[1].bar(yearly_categories, yearly_amounts, color=yearly_colors)
axs[1].set_title('Yearly Financial Overview')
axs[1].set_ylabel('Amount ($)')

# Adjust layout and display
plt.tight_layout()
plt.show()
