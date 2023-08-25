

class QueueOutOfRangeException(Exception):
    pass


class Queue:
    queues = {}
    def __init__(self, name, size):
        self.queue = []
        self.name = name
        self.size = size
        self.queues[name] = self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException
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
    
    def save(self):
        with open(f"{self.name}.txt", "w") as f:
            f.write(str(self.queue))
    
    @classmethod
    def load(cls, name):
        with open(f"{name}.txt", "r") as f:
            queue = cls(name, 10)
            queue.queue = eval(f.read())
            return queue
        

