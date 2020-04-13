import queue as Q
import math

track = {}
path = []  # stores final path from source to destination
max_queue = 0
expanded_nodes_count = 0


def astar(graph, coordinate_dict, start, goal, heu):
    global track
    global path
    global max_queue
    global expanded_nodes_count
    track = {}
    path = []
    max_queue = 0
    expanded_nodes_count = 0
    explored_list = []
    frontier = Q.PriorityQueue()  # initializing frontier

    heuristic = calc_heuristic(start, coordinate_dict, goal, heu)  # finding heuristic of  start
    frontier.put((heuristic, start))  # add start to frontier
    track[start] = ['start', 0, heuristic]  # keep value of parent, cost_from_start, total cost

    while not frontier.empty():
        max_queue = frontier.qsize()
        highest_priority = frontier.get()  # getting highest priority element based on heuristics
        if max_queue < frontier.qsize():
            max_queue = frontier.qsize()
        if highest_priority[1] == goal:  # checking for goal state
            give_path(goal, start)
            return expanded_nodes_count, max_queue + 1, len(path), path
        explored_list.append(highest_priority[1])  # appending to expanded nodes

        # finding children
        successors = find_children(graph, highest_priority[1])

        # finding heuristic of children
        for s in successors:
            s_heuristic = calc_heuristic(s, coordinate_dict, goal, heu)  # calculate heuristic
            parent = successors[s][0]
            cost_from_start = float(track[parent][1]) + float(successors[s][1]['cost'])
            total = cost_from_start + s_heuristic
            if s not in track.keys() and s not in explored_list:
                track[s] = [parent, cost_from_start, total]
                frontier.put((total, s))
            elif s in track.keys():
                if cost_from_start < track[s][1]:
                    track[s][1] = float(cost_from_start)
                    track[s][0] = parent


def calc_heuristic(node, coordinate_dict, goal, heu):
    s_dict = coordinate_dict[node]
    s_dict = s_dict.split(',')
    latitude_start = float(s_dict[0])
    longitude_start = float(s_dict[1])

    s_dict = coordinate_dict[goal]
    s_dict = s_dict.split(',')
    latitude_goal = float(s_dict[0])
    longitude_goal = float(s_dict[1])

    if heu == 0:
        heuristic = math.sqrt((69.5 * (latitude_start - latitude_goal)) ** 2 + (
                69.5 * math.cos((latitude_start + latitude_goal) / 360 * math.pi) * (
                longitude_start - longitude_goal)) ** 2)
    else:
        dLat = math.radians(latitude_goal - latitude_start)
        dLon = math.radians(longitude_goal - longitude_start)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(latitude_goal)) * math.cos(
            math.radians(latitude_start)) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        heuristic = 6371 * c
        heuristic = heuristic/2
    return heuristic


def find_children(graph, node):
    global expanded_nodes_count
    expanded_nodes_count += 1
    child_nodes = {}
    for n in graph.adj[node]:
        child_nodes[n] = (node, graph.edges[n, node])  # key = child and value is parent , cost from parent to node
    return child_nodes


def give_path(goal, start):
    path.append(goal)
    if goal == start:
        path.reverse()
        return
    goal = track[goal][0]
    give_path(goal, start)
