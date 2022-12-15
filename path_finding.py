import heapq


def path_finding_dijkstra(board):
    def get_neighbors(i, j):
        pass

    m = len(board)
    n = len(board[0])

    heap = []
    heapq.heappush(heap, (board[0][0], (0, 0)))

    unvisiteds = set()
    for i in range(m):
        for j in range(n):
            unvisiteds.add((i, j))

    distances = {}
    for i in range(m):
        for i in range(n):
            distances[(i, j)] = float('inf')
    distances[(0, 0)] = board[0][0]

    while heap:
        distance, work_node = heapq.heappop(heap)

        if work_node in unvisiteds:

