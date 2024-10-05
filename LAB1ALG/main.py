#АТД «очередь» - задача коммивояжера, исчерпывающий поиск в ширину
from abc import ABC, abstractmethod
import random
#генерация расстояний до городов
a = random.randint(1, 100)#0
b = random.randint(1, 100)#1
c = random.randint(1, 100)#2
d = random.randint(1, 100)#3

#словарь с городами и расстояниями до соседей
graph = {
    0: {1: b, 2: c, 3: d},
    1: {0: a, 2: c, 3: d},
    2: {0: a, 1: b, 3: d},
    3: {0: a, 1: b, 2: c}
}
print('\n', graph[0], '\n', graph[1], '\n', graph[2], '\n', graph[3],'\n')
#создание абстрактного класса
class AbstractQueue(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __del__(self):
        pass
    @abstractmethod
    def add(self, other):
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
class Queue(AbstractQueue): #создание_очереди наследование от абстрактного класса
    def __init__(self):#конструктор
        self.items = []
    def __del__(self):#деструктор
        pass
    def add(self,item):#добавление элемента
        self.items.append(item)
    def remove(self):#удаление левого элемента
        if not self.empty():
            return self.items.pop(0)
        else:#проверка не удалем ли мы элемент из пустой очереди
            raise IndexError("извлечение из пустой очереди")
    def size(self):#нахождение размера очереди
        return len(self.items)
    def empty(self):#проверка на пустоту очереди
        return len(self.items) == 0
def bfs(cities, start):#алгоритм
    best_distance = float('inf')
    best_route = None
    queue = Queue()#создание очереди
    queue.add((start, [start], 0))#добавляем кортеж содержащий начальный город, расстояние и пройденное расстояние
    while not queue.empty():
        city, route, distance = queue.remove()#распаковка
        if len(route) == len(cities):#если все города пройдены
            if distance+cities[city][start] < best_distance:
                best_distance = distance + cities[city][start]
                best_route = route + [start]#возвращаемся в начальный город
        else:
            for neighbor, cost in cities[city].items():#берем соседний город
                if neighbor not in route:
                    new_route = route +[neighbor]
                    new_distance = distance + cost
                    queue.add((neighbor, new_route, new_distance))
    return best_route,  best_distance

short, distance = bfs(graph, 0)
print(f'shortest route: {short}')
print(f'best distance is: {distance}')
