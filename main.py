import pickle
import logging
import argparse
import requests
from api_handler import crypto_service
from constants import LOG_FORMAT, CACHE_TIME_LIMIT
from context_manager import FileContextManager
from iterator import fetch_crypto_value, list_all_cryptocurrencies
from setting import LOG_FILE_PATH, CACHE_FILE_PATH, LAST_UPDATE_FILE_PATH
from utilس import record_ttl, check_if_cache_expired

logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE_PATH, format=LOG_FORMAT)

cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("-c", "--currency", type=str, help="Name of the cryptocurrency")
cli_args = cli_parser.parse_args()

def handle_cli_input() -> None:
    crypto_name = getattr(cli_args, 'currency', None)
    if crypto_ name:
        price = fetch_crypto_value(crypto_name)
        if price:
            print(f"{crypto_name}: {price}")
            logging.info(f"Valid  name '{crypto_name}'")
        else:
            print(f"Invalid name: {crypto_name}")
            logging.info(f"Invalid name '{crypto_name}'")
    else:
        list_all_cryptocurrencies()

if __name__ == "__main__":
    cache_expired, time_since_last_update = check_if_cache_expired(CACHE_TIME_LIMIT, LAST_UPDATE_FILE_PATH)
    if cache_expired:
        try:
            crypto_service.request_data()  
        except requests.RequestException as e:
            logging.exception("An error occurred during the API request: %s", e)

        if crypto_service.response_status == 200:
            with FileContextManager(CACHE_FILE_PATH, "wb") as cache_file:
                pickle.dump(crypto_service.response_data, cache_file)
                record_ttl(LAST_UPDATE_FILE_PATH)
                logging.info("Cache has been updated.")
        else:
            logging.error("API request failed. Status code: %s", crypto_service.response_status)
            logging.info("Cache not updated. Last update was %s seconds ago.", time_since_last_update)
    else:
        logging.info("Cache is valid. Last update was %s seconds ago.", time_since_last_update)

    with FileContextManager(CACHE_FILE_PATH, "rb") as cache_file:
        cached_crypto_data = pickle.load(cache_file)

    handle_cli_input()
