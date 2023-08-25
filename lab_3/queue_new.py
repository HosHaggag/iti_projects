
class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)
    
    def __repr__(self):
        return str(self.queue)
    
