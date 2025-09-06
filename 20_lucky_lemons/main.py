import random
import sys


# 1. Create the blueprint
class SlotMachine:
    def __init__(self, remaining_credits: int) -> None:
        self.credits = remaining_credits
        self.symbols: dict[str, int] = {'🍒': 1, '🍊': 2, '🍋': 5}

    def spin(self, bet: int) -> None:
        # Make sure the user has enough credits
        if self.credits >= bet:
            self.update_credits(-bet)
        else:
            print('Not enough credits...')
            return

        # Spin and add 3 symbols to a list
        result: list[str] = []
        for i in range(3):
            # time.sleep(.3)
            landed: str = random.choice(list(self.symbols))
            print(landed, end='')
            result.append(landed)

        print()

        # Check the winnings of the result
        winnings: int = self.calculate_winnings(result, bet)
        print(f'Credits won: {winnings}')

        # Check if the user can continue playing
        if self.credits == 0:
            print('Game over!')
            sys.exit()
        else:
            self.credits += winnings
            print(f'Credits remaining: {self.credits}')
            print('-' * 30)

    def calculate_winnings(self, result: list[str], bet: int) -> int:
        previous: str = result[0]
        winnings: list[int] = []

        # The user must get 3 in a row to win
        for symbol in result:
            if symbol == previous:
                winnings.append(self.symbols[symbol])
            else:
                winnings.clear()
                break

        # The reward is the sum of the winnings * the bet
        return sum(winnings) * bet

    # Helper function to update the credits
    def update_credits(self, amount: int) -> None:
        self.credits += amount

    # A method that starts the game
    def play(self) -> None:
        print(f'Starting credits: {self.credits}')
        print('-' * 30)
        while True:
            try:
                bet: int = int(input('Bet: '))
                self.spin(bet)
            except ValueError:
                print('Please enter a valid number...')


# 2. Run the code and play the game
if __name__ == "__main__":
    pokies: SlotMachine = SlotMachine(200)
    pokies.play()

# Homework:
# 1. Add a system that awards a player some credits for getting two in a row. Credits should only
# be awarded if the first two slots are matching.
# 2. If you're feeling adventurous, adds a fourth symbol to the game.
