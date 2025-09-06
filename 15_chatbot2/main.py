from datetime import datetime

"""
V2
ADDS HISTORY TO CHATS AND ALSO TAKES AN OOP APPROACH
"""

# ------------ helper (unchanged style) ------------
def contains(terms: list[str], content: str) -> bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())
    return any(matches)

# ------------ ChatBot class ------------
class ChatBot:
    def __init__(self, name: str) -> None:
        self.history: list[str] = []
        self.name = name

    # --- main reply method ---
    def response(self, text: str) -> str:
        text_lower = text.lower()

        # 1. follow-up: if user says "tomorrow" right after asking weather
        if contains(['tomorrow'], text_lower) and contains(['weather'], self.history[-1]):
            return "Tomorrow looks sunny with a high of 25 °C."

        # 2. normal intents
        if contains(['hello', 'hi'], text_lower):
            return 'Hello there!'
        elif contains(['goodbye', 'bye'], text_lower):
            return 'Talk to you later!'
        elif contains(['what time is it', 'current time'], text_lower):
            return f'The time is: {datetime.now().strftime("%H:%M:%S")}'
        elif contains(['weather'], text_lower):
            return "It’s partly cloudy and 22 °C right now."
        elif contains(['help', 'commands'], text_lower):
            return ('I understand: hello/hi, goodbye/bye, what time is it/current time, '
                    'weather, tomorrow (after weather), and help/commands.')

        return "Sorry... I can't answer that right now."

    # --- stores each user line, trims list to last 2 ---
    def remember(self, text: str) -> None:
        self.history.append(text.lower())
        if len(self.history) > 2:
            # keep only most-recent 2 messages
            self.history.pop(0)


    def run(self) -> None:
        print("Type 'help' for commands. Type 'bye' to quit.\n")
        while True:
            user_input: str = input('You: ')
            bot_reply = bot.response(user_input)
            print(f'{self.name}:', bot_reply)

            # exit if user said goodbye
            if contains(['bye', 'goodbye'], user_input):
                break

            # remember after responding
            bot.remember(user_input)

# ------------ run the chat loop ------------
if __name__ == "__main__":
    bot = ChatBot('Bob')
    bot.run()


