import string


class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] = self.load_common_passwords()

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r', encoding='utf-8') as file:
            return {line.strip() for line in file if line.strip()}

    @staticmethod
    def has_uppercase(password: str) -> bool:
        return any(c.isupper() for c in password)

    @staticmethod
    def has_symbol(password: str) -> bool:
        return any(c in string.punctuation for c in password)

    @staticmethod
    def is_long_enough(password: str) -> bool:
        return len(password) >= 10

    def rate(self, password: str) -> str:
        if self.is_common(password):
            return 'poor'
        score: int = 0
        if self.has_uppercase(password):
            score += 1
        if self.has_symbol(password):
            score += 1
        if self.is_long_enough(password):
            score += 1

        if score == 3:
            return 'secure'
        elif score == 2:
            return 'medium'
        else:
            return 'poor'


def main() -> None:
    # Link: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        if validator.is_common(password):
            print('❌ That is one of the top 10.000 most common passwords...')
            continue

        rating: str = validator.rate(password)
        if rating == 'secure':
            print('✅ Your password is secure! ')
        elif rating == 'medium':
            print('❌ Your password is of medium strength.')
        else:
            print('❌ Try adding symbols, uppercase letters, and increasing the length.')


if __name__ == '__main__':
    main()
