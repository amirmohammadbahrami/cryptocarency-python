import logging
import pickle
import time
from typing import List, Dict
from cryptocurrency import Cryptocurrency
from setting import LOGGER_DIR, CRYPTO_DATA_DIR
from context_manager import PickleContextManager

FORMAT= "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.DEBUG, filename=LOGGER_DIR, format=FORMAT)

class FileIterator:
    def __init__(self, file_data: List[Dict]) -> None:
        self.file_data = file_data
        self.index = -1 # for indexing in __next__.

    def __iter__(self):
        return self

    def __next__(self) -> Cryptocurrency:
        self.index += 1
        if self.index < len(self.file_data):
            return self.file_data[self.index]
        raise StopIteration

with PickleContextManager(CRYPTO_DATA_DIR, "rb") as file:
    data = pickle.load(file)

crypto_iterator = FileIterator(data)

def get_crypto_price(name: str):
    """
    returns crypto price if crypto name is valid else returns None
    """
    for crypto in crypto_iterator :
        if crypto["name"] == name:
            return crypto['current_price']

def print_all_cryptos():
    for crypto in crypto_iterator:
        print(f"{crypto['name']}: {crypto['current_price']}")
        time.sleep(1)
