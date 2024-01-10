from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, x, y):
        self.graph[x].append(y)

    def DFS_util(self, root, visited):
        if root not in visited:
            print(root, end=" -> ")
            visited.append(root)

        for i in range(len(self.graph[root])):
            if self.graph[root][i] not in visited:
                self.DFS_util(self.graph[root][i], visited)
                
    def DFS(self, root):
        visited = []
        self.DFS_util(root, visited)

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
