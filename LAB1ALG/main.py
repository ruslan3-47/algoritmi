#АТД «очередь» - задача коммивояжера, исчерпывающий поиск в ширину
from abc import ABC, abstractmethod
class AbstractQueue(ABC):
    @abstractmethod
    def __int__(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass
    @abstractmethod
    def remove(self):
        pass
    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def empty(self):
        pass
class Queue(AbstractQueue): #создание_очереди
    def __init__(self):
        self.items = []
    def add(self,item):
        self.items.append(item)
    def remove(self):
        if not self.empty():
            return self.items.pop(0)
        else:
            raise IndexError("pop from empty queue")
    def size(self):
        return len(self.items)
    def empty(self):
        return len(self.items)==0
def bfs(cities, start):#alg
    best_distance = float('inf')
    best_route = None
    queue = Queue()
    queue.add((start,[start],0))#add tuple
    while not queue.empty():
        city, route, distance = queue.remove()
        if len(route) == len(cities):#if all city done
            if distance<best_distance:
                best_distance = distance
                best_route = route + [start]#back in start
        else:
            for neighbor, cost in cities[city].items():#check neighbor
                if neighbor not in route:
                    route = route +[neighbor]
                    distance = distance + cost
                    queue.add((neighbor,route,distance))
    return best_route,  best_distance

graph = {
    0:{1: 10, 2: 15},
    1:{0: 10, 2: 5,3: 20},
    2:{0: 15, 1: 5,3: 12},
    3:{1: 20, 3: 12}
} #вершины и связи
short, distance = bfs(graph,0)
print(f'shortest route : {short}')
print(f'best distance is : {distance}')


