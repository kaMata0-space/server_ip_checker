from ip_checker.checker import Checker
from sender_bot.sender import Sender


def 

def main() -> None:
    checker = Checker()
    sender = Sender()
    new_hostname = checker()
    if new_hostname:
        print(f'New hostname: {new_hostname}')
    else:
        print(f'Old hostname')


if __name__ == '__main__':
    main()
