from datetime import datetime
from time import sleep
import sys

second = int(sys.argv[-1])


def get_arg_in_args(count: int):
    while count:
        print(f'{datetime.now()} seconds\n')
        sleep(1)
        count -= 1


get_arg_in_args(second)
