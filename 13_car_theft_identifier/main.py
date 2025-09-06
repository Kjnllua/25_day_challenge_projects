class Car:
    def __init__(self, licence_plate: str):
        if len(licence_plate) != 6:
            raise ValueError('Invalid licence plate.')

        self.license_plate = licence_plate


class StolenCarRegistry:
    def __init__(self) -> None:
        # Example: Set of license plates that are stolen
        self.stolen_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def is_stolen(self, plate: str) -> bool:
        return plate.upper() in self.stolen_plates


def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()
    # Populate with some stolen plates
    registry.add_stolen_plates(['ABC123', 'XYZ999', 'BOB789'])

    print('Welcome to Car Theft Identifier')
    while True:
        plate: str = input('Enter car licence plate: ').strip()
        car: Car = Car(plate)
        if registry.is_stolen(car.license_plate):
            print(f'❌ Car with plate "{car.license_plate.upper()}" is: REPORTED STOLEN!')
        else:
            print(f'✅ Car with plate "{car.license_plate.upper()}" is: OK')


if __name__ == '__main__':
    main()
