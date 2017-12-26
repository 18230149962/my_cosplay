from edcone import run1
from edctwo import run2
from edcthree import run3
from edcfour import run4
from edcfive import run5
from edcsix import run6
import threading

if __name__ == '__main__':
    for i in range(200):
        threads = []
        threads.append(threading.Thread(target=run1))
        threads.append(threading.Thread(target=run2))
        threads.append(threading.Thread(target=run3))
        threads.append(threading.Thread(target=run4))
        threads.append(threading.Thread(target=run5))
        threads.append(threading.Thread(target=run6))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(i)
