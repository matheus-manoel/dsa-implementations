from collections import deque


def can_bicolor(graph):
    RED = 'red'
    BLUE = 'blue'

    colors = {}
    q = deque()

    q.append(0)
    colors[0] = RED

    while q:
        work_node = q.popleft()

        for neigh in graph[work_node]:
            expected_color = RED if colors[work_node] == BLUE else BLUE
            if neigh in colors:
                if colors[neigh] != expected_color:
                    return False
            else:
                q.append(neigh)
                colors[neigh] = expected_color

    return True


my_graph_false = {
    0: [1, 4],
    1: [0, 2],
    2: [1, 3],
    3: [4, 2],
    4: [0, 3]
}
my_graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
}
print(can_bicolor(my_graph))
