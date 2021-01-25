class Queue:
    def __init__(self):
        self.elements = np.array([])

    def enqueue(self, elem):
        self.elements = np.append(self.elements, elem)

    def dequeue(self, elem):
        if (self.isEmpty()):
            elem = self.elements[0]
            self.elements = self.elements[1:]

            return elem

    def isEmpty(self):
        if (len(self.elements == 0)):
            return true
        else:
            return false
