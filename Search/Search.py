import sys
import DFS
import astar
import rbfs
import creategraph as cg

mini = 0
def main():

    # Accepting arguments from the command line
    search_type = sys.argv[1]
    heuristic = sys.argv[2]
    start = sys.argv[3]
    goal = sys.argv[4]

    # constructing graph given cities and distances between the cities in the files roads.txt and coordinates.txt
    graph, coordinate_dict, a = cg.creategraph("roads.txt", "coordinates.txt")

    # calling of respective methods from file
    if search_type.lower() == "dfs":
        cities_expanded, max_queue_size, final_path_length, final_path = DFS.dfs(graph, start, goal)

    elif search_type.lower().startswith("a") or search_type.lower().endswith("*"):
        cities_expanded, max_queue_size, final_path_length, final_path = astar.astar(graph, coordinate_dict, start,
                                                                                     goal, heuristic)

    elif search_type.lower() == "rbfs":
        cities_expanded, max_queue_size, final_path_length, final_path = rbfs.rbfs(graph, coordinate_dict, start, goal,
                                                                                   heuristic)
    else:
        print("No Algorithm with " + search_type + " name found. Please use DFS, A* or RBFS")
        return

    print(cities_expanded)
    print(max_queue_size)
    print(final_path_length)
    print(final_path)

if __name__ == '__main__':
    main()
