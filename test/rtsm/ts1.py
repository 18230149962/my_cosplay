import threading
from llll import zz
from nnn import sy

if __name__ == '__main__':
    for z in range(10):
        threads = []
        threads.append(threading.Thread(target=sy()))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
