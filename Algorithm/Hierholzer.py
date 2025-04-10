class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        # Default dictionary to store graph
        self.graph = {i: [] for i in range(vertices)}

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to remove edge from graph
    def removeEdge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    # Function to check if all non-zero degree vertices are connected
    def isConnected(self):
        visited = [False] * self.V
        # Find a vertex with non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break

        # If there are no edges in the graph, return True
        if i == self.V - 1:
            return True

        # Start DFS traversal from a vertex with non-zero degree
        self.DFSUtil(i, visited)

        # Check if all non-zero degree vertices are visited
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True

    # A function used by isConnected()
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Function to run Hierholzer's algorithm
    def printEulerTour(self):
        # Check if all non-zero degree vertices are connected
        if self.isConnected() == False:
            print("Graph is not Eulerian")
            return

        # Find a vertex with odd degree
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) & 1:
                u = i
                break

        # Print tour starting from odd vertex
        print(self.printEulerUtil(u))

    # Function to run Hierholzer's algorithm starting from vertex u
    def printEulerUtil(self, u):
        # Print current vertex
        result = str(u)
        while len(self.graph[u]) > 0:
            # Find adjacent vertex of u
            v = self.graph[u].pop()
            # If edge u-v is not removed and it's a valid next edge
            self.removeEdge(u, v)
            result += self.printEulerUtil(v)

        return result

# Example usage:
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.printEulerTour()