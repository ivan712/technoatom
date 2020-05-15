import threading
import time

def potoc(name):
    print("Thread "+str(name)+" have started!")
    time.sleep(4)
    print("Thread "+str(name)+" have stoped!")



print("Make thread")
x = threading.Thread(target=potoc,args=(1,))
print("start thread")
x.start()
x.join()
print("Waiting thread finish")
print("The End")
