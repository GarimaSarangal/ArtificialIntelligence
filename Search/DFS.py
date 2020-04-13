from collections import deque

frontier = deque()  # stack
path = []  # path traversed
reverselist = []
nodes_expanded_count = 0


def dfs(graph, start, goal):
    global nodes_expanded_count
    global path
    path = []
    nodes_expanded_count = 0
    frontier.append(start)
    max_length = len(frontier)
    while frontier:
        if max_length < len(frontier):
            max_length = len(frontier)
        next_node = frontier.pop()
        if next_node == goal:
            path.append(goal)
            return nodes_expanded_count, max_length, len(path), path
        if next_node in path:
            continue
        path.append(next_node)
        neighbors = graph.neighbors(next_node)
        nodes_expanded_count += 1
        reverselist.clear()
        for n in neighbors:
            if n in path:
                continue
            reverselist.append(n)
        reverselist.reverse()
        for n in reverselist:
            frontier.append(n)

    return nodes_expanded_count, max_length, len(path), path;
