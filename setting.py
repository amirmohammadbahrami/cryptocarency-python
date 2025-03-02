from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

DATA_DIC = Path.joinpath(BASE_DIR, "data")
LOGGER_DIC = Path.joinpath(BASE_DIR, "data/logger.log")
CRYPTO_DATA = Path.joinpath(BASE_DIR, "data/crypto_data.pkl")
LAST_UPDATE= Path.joinpath(BASE_DIR, "data/last_update.txt")