class Queue: #создание_очереди
    def __init__(self):
        self.way = []
    def add(self,way):
        self.way.insert(0,way)
    def remove(self):
        return self.way.pop()
    def size(self):
        return len(self.way)
class cities:
    def __init__(self, name, connect):
        self.name= name
        self.connect = connect
