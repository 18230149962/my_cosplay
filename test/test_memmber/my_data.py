from jianhua_gg import jianhuashizhazha
import threading

if __name__ == '__main__':
    for i in range(200):
        threads = []
        threads.append(threading.Thread(target=jianhuashizhazha))
        # threads.append(threading.Thread(target=run2))
        # threads.append(threading.Thread(target=run3))
        # threads.append(threading.Thread(target=run4))
        # threads.append(threading.Thread(target=run5))
        # threads.append(threading.Thread(target=run6))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(i)
