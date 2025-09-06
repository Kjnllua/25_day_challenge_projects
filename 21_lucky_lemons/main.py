import random
import sys


class SlotMachine:
    def __init__(self, remaining_credits: int) -> None:
        self.credits = remaining_credits
        self.symbols: dict[str, int] = {'🍒': 1, '🍊': 2, '🍋': 5}

    def spin(self, bet: int) -> None:
        if self.credits >= bet:
            self.update_credits(-bet)
        else:
            print('Not enough credits...')
            return

        result: list[str] = []

        for i in range(3):
            # time.sleep(.3)
            landed: str = random.choice(list(self.symbols))
            print(landed, end='')
            result.append(landed)

        print()
        winnings: int = self.calculate_winnings(result, bet)
        print(f'Credits won: {winnings}')
        if self.credits == 0:
            print('Game over!')
            sys.exit()
        else:
            self.credits += winnings
            print(f'Credits remaining: {self.credits}')
            self.divider()

    def calculate_winnings(self, result: list[str], bet: int) -> int:
        previous: str = result[0]
        winnings: list[int] = []

        for symbol in result:
            if symbol == previous:
                winnings.append(self.symbols[symbol])
            else:
                winnings.clear()
                break

        return sum(winnings) * bet

    def update_credits(self, amount: int) -> None:
        self.credits += amount

    def play(self) -> None:
        print(f'Starting credits: {self.credits}')
        self.divider()
        while True:
            try:
                bet: int = int(input('Bet: '))
                self.spin(bet)
            except ValueError:
                print('Please enter a valid number...')

    @staticmethod
    def divider() -> None:
        print('-' * 30)


if __name__ == "__main__":
    pokies: SlotMachine = SlotMachine(200)
    pokies.play()
