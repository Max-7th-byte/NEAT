from queue import Queue

my_queue = Queue()
my_queue.put('Max')
my_queue.put('Is')
my_queue.put('Shit')

while not my_queue.empty():
    print(my_queue.get())