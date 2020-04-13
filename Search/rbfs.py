import math

expanded_nodes_count = 0  # counts the number of nodes expanded
max_queue = 0


def rbfs(graph, coordinate_dict, start, goal, heu):
    global expanded_nodes_count
    global max_queue
    expanded_nodes_count = 0
    max_queue = 0
    heuristic = calc_heuristic(start, coordinate_dict, goal, heu)  # finding heuristic of  start
    first = [start, heuristic]
    path, r = search(graph, coordinate_dict, first, goal, heu, start, now_q_size=0, now_cost=0, f_limit=math.inf)
    return expanded_nodes_count, max_queue, len(path), path


def search(graph, coordinate_dict, current, goal, heu, parent, now_q_size, now_cost=0, f_limit=math.inf):
    global max_queue
    global expanded_nodes_count

    if current[0] == goal:
        if max_queue < now_q_size:
            max_queue = now_q_size
        return [current[0]], 0

    successors = []
    neighbours = graph.adj[current[0]]  #finding neighbors
    expanded_nodes_count += 1           # counting number of nodes expanded

    for s in neighbours:
        if s == parent:
            continue
        s_heuristic = calc_heuristic(s, coordinate_dict, goal, heu)  # calculate heuristic
        cost_from_start = float(now_cost) + float(graph.edges[s, current[0]]['cost'])
        f_val = cost_from_start + s_heuristic
        successors.append([s, max(f_val, current[1])])          # adding successors

    if not successors:
        if max_queue < now_q_size:
            max_queue = now_q_size
        return [], math.inf

    now_q_size += len(successors)

    while True:
        best = min(successors, key=lambda i: i[1])
        s_now_cost = now_cost + float(graph.edges[best[0], current[0]]['cost'])
        if best[1] > f_limit:
            if max_queue < now_q_size:
                max_queue = now_q_size
            return [], best[1]
        successors.remove(best)
        if len(successors) > 0:
            alternative = min(successors, key=lambda i: i[1])
            successors.append(best)
            result, best[1] = search(graph, coordinate_dict, best, goal, heu, current[0], now_q_size, s_now_cost,
                                     min(f_limit, alternative[1]))
        else:
            successors.append(best)
            result, best[1] = search(graph, coordinate_dict, best, goal, heu, current[0], now_q_size, s_now_cost,
                                     min(f_limit, best[1]))

        if result:
            final = list(result)
            final.insert(0, current[0])
            if max_queue < now_q_size:
                max_queue = now_q_size
            return final, 0


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
                69.5 * math.cos((latitude_start + latitude_goal) * math.pi / 360) * (
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
