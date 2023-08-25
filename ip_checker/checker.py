import os.path
import subprocess
from typing import Optional


class Checker:

    def __init__(self, storage_file_path: Optional[str] = './last_ip_address.txt'):
        self.storage_file_path = storage_file_path
        self.hostname = None

    def update_hostname(self) -> None:
        self.hostname = subprocess.check_output('hostname -I', shell=True).decode('utf-8').split('\n')[0]

    def get_last_hostname(self) -> str:
        with open(f'{self.storage_file_path}', 'r') as file_storage:
            last_hostname = file_storage.read()
        return last_hostname

    def write_new_hostname(self) -> None:
        with open(f'{self.storage_file_path}', 'w') as file_storage:
            file_storage.write(self.hostname)

    def create_storage_file(self) -> None:
        sf = open(f'{self.storage_file_path}', 'w')
        sf.close()

    def __call__(self, *args, **kwargs) -> str:
        if not os.path.exists(self.storage_file_path):
            self.create_storage_file()
        self.update_hostname()
        last_hostname = self.get_last_hostname()
        if self.hostname and self.hostname != last_hostname:
            self.write_new_hostname()
            return self.hostname
