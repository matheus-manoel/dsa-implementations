from collections import deque


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, src, dst, weight=1):
        if src not in self.edges:
            self.edges[src] = [(dst, weight)]
        else:
            self.edges[src].append((dst, weight))

    def bfs(self, src):
        visiting_q = deque()

        visiting_q.append(src)
        visited = set(src)

        distance = {src: 0}
        predecessor = {src: None}

        while visiting_q:
            work_node = visiting_q.popleft()

            for neighbour, _ in self.edges[work_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    visiting_q.append(neighbour)
                    distance[neighbour] = distance[work_node] + 1
                    predecessor[neighbour] = work_node

    def dfs(self, src, visited=set()):
        visited.add(src)
        for neighbour, _ in self.edges[src]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
