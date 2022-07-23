class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def add(self, v):
        self.queue.append(v)
    
    def delete(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isempty(self):
        return self.queue == []
    
    def __str__(self):
        return(str(self.queue))