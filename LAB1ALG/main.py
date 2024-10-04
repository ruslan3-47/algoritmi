#АТД «очередь» - задача коммивояжера, исчерпывающий поиск в ширину
class Queue: #создание_очереди
    def __init__(self):
        self.way = []
    def add(self,way):
        self.way.insert(0,way)
    def remove(self):
        return self.way.pop()
    def size(self):
        return len(self.way)
    def empty(self):
        return len(self.way)==0
def bfs(graph, beggin):
    queue = Queue()  # не посещенные вершины
    queue.add(beggin)
    visited = set()  # посещенные
    visited.add(beggin)  # добавляем начальную вершину
    while queue.empty()!=1:
        v = queue.remove()
        print(v,end=' ')
        for vertex in graph[v]:#осматриваем окрестности вершин
            if vertex not in visited:
                visited.add(vertex)
                queue.add(vertex)

graph = {0:[1, 3],1:[0, 2],2:[0,1,4],3:[0],4:[2]} #вершины и связи
bfs(graph,0)


