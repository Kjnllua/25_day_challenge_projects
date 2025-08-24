print('Welcome to Expense Splitter™!')
total_bill: float = float(input('1. Enter the total bill you would like to split: '))

# Getting the participants
people: list[str] = []
print('2. Add participants (press Enter on an empty line when finished):')
while True:
    input_name: str = input('Name: ').lower()
    if input_name.strip() == '':
        break

    if input_name in people:
        print('That name is already listed. Please add a different name.')
    else:
        people.append(input_name)

# Splitting the bill
print('3. Now, specify the percentage each person will pay.\n'
      '(Type "even" at any time to split the bill equally.)')

people_dict: dict[str, float] = {}
total_percent: float = 100.0

for person in people:
    percent_input: str = input(f'[{total_percent:.0f}% remaining] {person.capitalize()}: ').lower()

    if percent_input.strip() == '':
        percent_input = '0'

    if percent_input == 'even':
        for nested_person in people:
            people_dict[nested_person] = (1 / len(people)) * total_bill
        break

    people_dict[person] = (float(percent_input) / 100) * total_bill
    total_percent -= float(percent_input)

# Displaying the information
print('\n--- Split Summary ---')
for name, share in people_dict.items():
    print(f'{name.capitalize():10}: ${share:,.2f}')
print('---------------------')

# Homework:
# 1. Handle what happens if the user taps on enter without specifying a total bill amount
# 2. Handle what happens if the user doesn't add and people to the bill
# 3. Make it so the user can only charge up to 100% of the bill
# 4. Add a field to the summary that tells the user the money that wasn't split by anyone
