# Get user input and calculate tax
base_income: float = float(input("Enter your yearly income: "))
tax_rate: float = float(input("Enter your tax rate percentage: ")) / 100
taxed: float = base_income * tax_rate

income_2x: float = base_income * 2
income_3x: float = base_income * 3

doubled_taxed: float = income_2x * tax_rate
tripled_taxed: float = income_3x * tax_rate

# Display the data
print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Base Income:              ${base_income:,.2f}")
print(f"Doubled Income:           ${income_2x:,.2f}")
print(f"Tripled Income:           ${income_3x:,.2f}")
print(f"Tax Rate:                 {tax_rate:.0%}")
print("-" * 40)
print(f"Yearly Tax (Base):        ${taxed:,.2f}")
print(f"Yearly Tax (Doubled):     ${doubled_taxed:,.2f}")
print(f"Yearly Tax (Tripled):     ${tripled_taxed:,.2f}")
print("=" * 40)
