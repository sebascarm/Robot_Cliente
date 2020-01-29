import threading
import time
from multiprocessing import Value


def proceso(run):
    while run.value:
        print(run.value)
        time.sleep(0.1)
    print("run False")


ejecucion = Value('b', True)
t = threading.Thread(target=proceso, args=(ejecucion,))
t.start()
time.sleep(1)
ejecucion.value = False
print("ejecucion FALSE")
#t.join()
#time.sleep(2)
