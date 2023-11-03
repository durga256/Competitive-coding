from collections import defaultdict

class Graph():
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self,a,b):
        self.graph[a].append(b)

    def DFS_util(self,v,visited):

        if v not in visited:
            print(v, end = " ")
            visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS_util(neighbour, visited)

    def DFS(self,v):
        visited = set()

        self.DFS_util(v,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
    
# Function call
g.DFS(0)
