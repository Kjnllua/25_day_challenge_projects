import json


# 1. Create instructions
def show_instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')


# 2. Load the data
def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        exchange_rates: dict[str, float] = json.load(file)
        return exchange_rates


# 3. Convert the currency
def convert_currency(user_input: str, currency_codes: list[str], exchange_rates: dict[str, float]) -> None:
    for currency_code in currency_codes:
        # Check if user entered a valid currency code
        if user_input.endswith(currency_code):
            try:
                # Extract amount by removing the 3-letter currency code
                input_amount: float = float(user_input[:-3])
            except ValueError:
                print('Invalid amount.')
                break

            # Get exchange rate for the input currency
            source_currency_rate: float = exchange_rates[currency_code]
            base_amount: float = input_amount / source_currency_rate

            # Display conversion results
            print(f'{int(input_amount):>16} {currency_code}')
            print('-' * 20)
            for target_currency in currency_codes:
                if target_currency == currency_code:  # Skip converting to same currency
                    continue
                converted_amount: float = base_amount * exchange_rates[target_currency]
                print(f'= {int(converted_amount):>14} {target_currency}')
            print('-' * 20)
            break
    else:
        print('Invalid input. Please check currency code.')


# 4. Put it all together
def main() -> None:
    # 1. Display instructions
    show_instructions()

    # 2. Load exchange rate data
    exchange_rates: dict[str, float] = load_exchange_rates()
    currency_codes: list[str] = list(exchange_rates.keys())

    while True:
        # 3. Get user input
        user_input: str = input('Convert: ').strip().upper()

        if user_input == 'LIST':
            print('Available currencies:', ', '.join(currency_codes))
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        # 4. Process currency conversion
        convert_currency(user_input, currency_codes, exchange_rates)


if __name__ == '__main__':
    main()
