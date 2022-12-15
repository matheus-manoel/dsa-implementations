import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        def build_graph():
            graph = {node: [] for node in range(1, n + 1)}

            for src, dst, wei in times:
                graph[src].append((dst, wei))

            return graph

        def dijkstra(graph, src):
            heap = [(0, src)]
            distances = {node: float('inf') for node in range(1, n+1)}
            distances[src] = 0
            unvisiteds = set(distances.keys())

            while heap:
                _, work_node = heapq.heappop(heap)

                if work_node in unvisiteds:
                    unvisiteds.remove(work_node)

                    for neigh, neigh_dist in graph[work_node]:
                        if neigh in unvisiteds:
                            new_dist = distances[work_node] + neigh_dist
                            if new_dist < distances[neigh]:
                                heapq.heappush(heap, (new_dist, neigh))
                                distances[neigh] = new_dist

            return max(distances.values()) if not unvisiteds else -1

        return dijkstra(build_graph(), k)
