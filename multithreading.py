import threading
def thread():
    for x in range(50):
        print("BULLETPROOF")

t1 = threading.Thread(target=thread)
t1.start()
