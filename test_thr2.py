import time
from thread_admin import ThreadAdmin


def proceso(run):
    while run.value:
        print("loop de ejecucion")
        time.sleep(0.5)
    


th = ThreadAdmin()
th.start(proceso,name="PROCESO", enviar_ejecucion=True)
time.sleep(5)
th.close()
time.sleep(3)
