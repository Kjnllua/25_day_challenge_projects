# 1. Get the user input for the total bill amount
print('Welcome to Expense Splitter™!')

while True:
    bill: str = input('1. Enter the total bill you would like to split: ')
    if bill == "":
        print("\n Please enter the total bill")
    else:
        total_bill: float = float(bill)
        break

# 2. Add the participants to the bill
people: list[str] = []
print('2. Add participants (press Enter on an empty line when finished):')
while True:
    input_name: str = input('Name: ').lower()
    if input_name.strip() == '':
        if len(people) == 0:
            print("\n Please add participant names")
            continue

        else:
            done: str = input("\n Are you done? (Yes) or (No): ")
            if done.strip().lower() == "yes":
                break
            else:
                continue
        # break

    # Check for duplicate names
    if input_name in people:
        print('That name is already listed. Please add a different name.')
    else:
        people.append(input_name)

# 3. Splitting the bill
print('3. Now, specify the percentage each person will pay.')
print('(Type "even" at any time to split the bill equally.)')

# Create a dictionary that holds how much each person owes
people_dict: dict[str, float] = {}
total_percent: float = 100.0

# Get inputs for each person
even_split: bool = False

for person in people:
    while True:
        percent_input: str = input(f'[{total_percent:.0f}% remaining] {person.capitalize()}: ').lower()
    
        # If you tap on enter, 0 will be the default value
        if percent_input.strip() == '':
            percent_input = '0'
    
        # Typing 'even' will split the bill evenly
        if percent_input.strip() == 'even':
            for nested_person in people:
                people_dict[nested_person] = (1 / len(people)) * total_bill
                even_split = True
    
        if float(percent_input) > total_percent:
            print("!!! Error: Input is greater than remaining percentage !!!")
        else:
            people_dict[person] = (float(percent_input) / 100) * total_bill
            total_percent -= float(percent_input)
            break

    if even_split:
        break

# 4. Display the information
print('\n--- Split Summary ---')
for name, share in people_dict.items():
    print(f'{name.capitalize():10}: ${share:,.2f}')
print('---------------------')
