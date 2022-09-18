from collections import deque
import heapq


class Graph:

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def add_edge(self, src, dst, weight=1):
        self.adj[src].append((dst, weight))
        self.E += 1

    def get_out_degree(self, src):
        return len(self.adj[src])

    # O(E)
    def get_in_degree(self, dst):
        n_of_edges_to_dst = 0
        for neighbours in self.adj:
            for neighbour in neighbours:
                if neighbour[0] == dst:
                    n_of_edges_to_dst += 1

        return n_of_edges_to_dst

    def bfs(self, src):
        q = deque()
        discovered = set()
        visiting_order = []

        q.append(src)
        discovered.add(src)

        while q:
            visiting = q.popleft()
            visiting_order.append(visiting)

            for neighbour in self.adj[visiting]:
                if neighbour[0] not in discovered:
                    discovered.add(neighbour[0])
                    q.append(neighbour[0])

        return visiting_order

    def dfs(self, src, visited=set()):
        visited.add(src)
        for neighbour in self.adj[src]:
            if neighbour[0] not in visited:
                self.dfs(neighbour[0], visited)

    def dfs_stack(self, src):
        discovered = set()
        stack = []

        discovered.add(src)
        stack.append(src)

        while stack:
            visiting = stack.pop()

            for neighbour in self.adj[visiting]:
                if neighbour[0] not in discovered:
                    discovered.add(neighbour[0])
                    stack.append(neighbour[0])

    def dijkstra_with_list(self, src):
        distances = [float('inf')] * self.V
        predecessors = [-1] * self.V
        unvisiteds = set(range(self.V))

        distances[src] = 0
        predecessors[src] = src
        visiting = src

        while unvisiteds:
            min_cost = float('inf')
            for node in unvisiteds:
                if distances[node] <= min_cost:
                    min_cost = distances[node]
                    visiting = node

            unvisiteds.remove(visiting)

            for neighbour, weight in self.adj[visiting]:
                if (neighbour in unvisiteds and
                        distances[visiting] + weight < distances[neighbour]):
                    distances[neighbour] = distances[visiting] + weight
                    predecessors[neighbour] = visiting

        return distances

    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        predecessors = [-1] * self.V
        unvisiteds = set(range(self.V))

        distances[src] = 0
        predecessors[src] = src

        heap = [(0, src)]

        while heap:
            _, visiting = heapq.heappop(heap)

            if visiting in unvisiteds:
                unvisiteds.remove(visiting)

                for neighbour, weight in self.adj[visiting]:
                    if (neighbour in unvisiteds and
                            distances[visiting] + weight < distances[neighbour]):
                        distances[neighbour] = distances[visiting] + weight
                        predecessors[neighbour] = visiting
                        heapq.heappush(heap, (distances[neighbour], neighbour))

        return distances

    def topological_sort(self):
        inDegrees = [0] * self.V
        for neighbours_list in self.adj:
            for neighbour, _ in neighbours_list:
                inDegrees[neighbour] += 1

        q = deque()
        for node, inDegree in enumerate(inDegrees):
            if inDegree == 0:
                q.append(node)

        result = []

        while q:
            work_node = q.popleft()
            result.append(work_node)

            for neighbour in self.adj[work_node]:
                inDegrees[neighbour] -= 1
                if inDegrees[neighbour] == 0:
                    q.append(neighbour)

        return result


g = Graph(6)
g.add_edge(1, 2, 6)
g.add_edge(1, 4, 1)
g.add_edge(2, 1, 6)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 2)
g.add_edge(2, 5, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 5, 5)
g.add_edge(4, 1, 1)
g.add_edge(4, 2, 2)
g.add_edge(4, 5, 1)
g.add_edge(5, 2, 2)
g.add_edge(5, 3, 5)
g.add_edge(5, 4, 1)
print(g.dijkstra(1))
