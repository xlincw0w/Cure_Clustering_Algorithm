import numpy as np


class Queue:
    def __init__(self):
        self.elements = np.array([])

    def enqueue(self, elem):
        self.elements = np.append(self.elements, elem)

    def dequeue(self):
        if (self.isEmpty()):
            elem = self.elements[0]
            self.elements = self.elements[1:]

            return elem

        else:
            print('Cannot dequeue an empty queue !')

    def isEmpty(self):
        if (len(self.elements == 0)):
            return True
        else:
            return False

    def logQueue(self):
        print('\nLogging queue')
        print(self.elements)
        print('\n\n')