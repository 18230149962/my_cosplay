import threading
i = 0
def zz():
    global i
    i += 1
    n = "01"+"%03d" % i
    print(n)


if __name__ == '__main__':
    for z in range(10):
        threads = []
        threads.append(threading.Thread(target=zz()))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()