__author__ = "Ejie Emmanuel Ebuka"

# Queue

from multiprocessing import Queue

myQueue = Queue(maxsize= 4)
myQueue.put(1)
print(myQueue.get())