import time
from typing import Union, Tuple
from os import PathLike

def has_time_passed(limit: Union[int, float, str], file_path: Union[str, PathLike]) -> Tuple[bool, float]:
   
    try:
        with open(file_path, "r") as file:
            last_time = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return True, float("inf") 

    elapsed_time = time.time() - last_time
    return elapsed_time > float(limit), elapsed_time


def update_timestamp(file_path: Union[str, PathLike]):
  
    with open(file_path, "w") as file:
        file.write(str(int(time.t
                           )))
