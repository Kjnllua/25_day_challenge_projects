import json


# Prints instructions
def instructions() -> None:
    print("1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.")
    print("2. Type LIST to list available currencies.")
    print('3. Type QUIT to exit.')


# Loads json data
def load_data() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        rates: dict[str, float] = json.load(file)
        return rates


# Converts one currency into many others
def convert(user_input: str, codes: list[str], rates: dict[str, float]) -> None:
    for code in codes:
        # Checks to see if the user entered a valid currency code
        if user_input.endswith(code):
            try:
                # Removes the currency code from the input
                amount: float = float(user_input[:-3])
            except ValueError:
                print('Invalid amount.')
                break

            # Gets the rate code the current code
            in_rate: float = rates[code]
            base_val: float = amount / in_rate  # Calculates the value in USD by default

            # Display conversions
            print(f'{int(amount):>16} {code}')
            print('-' * 20)
            for c2 in codes:
                if c2 == code:  # Do not convert base value to base value
                    continue
                out_val: float = base_val * rates[c2]
                print(f"= {int(out_val):>14} {c2}")
            print('-' * 20)
            break
    else:
        print("Invalid input. ")


def main() -> None:
    # 1. Display instructions
    instructions()

    # 2. Load data
    rates: dict[str, float] = load_data()
    codes: list[str] = list(rates.keys())

    while True:
        # 3. Take user input
        user_input: str = input("> ").strip().upper()
        if user_input == "LIST":
            print("Available currencies:", ", ".join(codes))
            continue
        elif user_input == "QUIT":
            print("Exiting.")
            break
        # 4. Parse amount and currency
        convert(user_input, codes, rates)


if __name__ == '__main__':
    main()
