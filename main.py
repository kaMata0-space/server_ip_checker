from ip_checker.checker import Checker


def main() -> None:
    checker = Checker()
    new_hostname = checker()
    if new_hostname:
        print(f'New hostname: {new_hostname}')
    else:
        print(f'Old hostname')


if __name__ == '__main__':
    main()
