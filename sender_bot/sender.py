import telebot


class Sender:

    def __init__(self, api_token: str) -> None:
        self.api_token = api_token
        self.bot = telebot.TeleBot(api_token)

    def send_message(self, uid: int) -> None:
        self.bot.send_message(uid, "Hello")
