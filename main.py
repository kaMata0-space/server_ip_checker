import os

from ip_checker.checker import Checker
from sender_bot.sender import Sender
from load_env import load_environ


def main() -> None:
    checker = Checker()
    sender = Sender(api_token=os.getenv('BOT_API_TOKEN'))
    new_hostname = checker()
    if new_hostname:
        sender.send_message(uid=int(os.getenv('ADMIN_TELEGRAM_UID')), message=f'New hostname: {new_hostname}')
    else:
        sender.send_message(uid=int(os.getenv('ADMIN_TELEGRAM_UID')), message=f'Old hostname.')


if __name__ == '__main__':
    load_environ()
    main()
