from sj import xlszz
# from ssz  import xlssx
from Pone import xlssx
import threading
from functools import wraps


if __name__ == '__main__':
    for i in range(62):
        threads = []
        # threads.append(threading.Thread(target=xlszz))
        threads.append(threading.Thread(target=xlssx))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(i)