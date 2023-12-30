import threading

def print_hello():
    print("Hello")

def print_hi():
    print("Hi")

# Create threads
thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_hi)

# Start threads
thread1.start()
thread2.start()


# Wait for threads to finish (optional, but recommended for synchronization)
thread1.join()
thread2.join()