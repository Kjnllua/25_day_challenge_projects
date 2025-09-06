# WIP
from collections import Counter
from time import sleep


# Create a car blueprint
class Car:
    def __init__(self, brand: str, color: str, model: int) -> None:
        self.brand = brand
        self.color = color
        self.model = model

    def drive(self, distance: int, speed: int) -> None:
        print(f'{self.brand} {self.model} [{self.color}] started journey...')
        for i in range(1, distance + 1):
            sleep(60 / speed)
            print(f'KM: {i}')

        print(f'{self.brand} {self.model} [{self.color}] completed journey...')


# Test that the car works
def test_car() -> None:
    volvo: Car = Car('Volvo', 'Red', 200)
    volvo.drive(6, 140)


# Create a car factory
cars: list[Car] = [Car('Volvo', 'Red', 200),
                   Car('Volvo', 'Red', 200),
                   Car('Volvo', 'Red', 200), ]


def create_cars() -> None:
    # Everything is case-sensitive here
    brand: str = input('Enter the brand: ')
    color: str = input('Enter the color: ')
    try:
        model: int = int(input('Enter the model number: '))
        amount: int = int(input('Enter the amount: '))

        for i in range(amount):
            cars.append(Car(brand, color, model))

        print('Cars created!')
    except ValueError:
        print('Error, please enter numbers as digits only.')


def display_stock() -> None:
    car_tuples: list[tuple[str, str, int]] = [(car.brand, car.color, car.model) for car in cars]
    counter: Counter[tuple[str, str, int]] = Counter(car_tuples)

    for (brand, model, color), count in counter.items():
        print(f'{brand} {model} [{color}]: {count}')


print('Type: "create" to create cars and "display" to display current stock')
while True:
    user_input: str = input('You: ').lower().strip()

    if user_input == 'create':
        create_cars()
    elif user_input == 'display':
        display_stock()
    else:
        print(f'Unknown command: "{user_input}"')

# Homework:
# 1. Add a function that allows you to sell cars:
# - It must be able to check stock and only sell if there's enough cars
# 2. Create a bank to store the money you're making with your car sales
