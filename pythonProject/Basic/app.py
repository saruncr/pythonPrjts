import threading
import time

done = False


def worker():
    counter = 0
    while not done:
        counter += 1
        print(counter)
        time.sleep(1)


threading.Thread(target=worker).start()

input("Press Enter to exit")
done = True

