import networkx as nx


def creategraph(filename1, filename2):
    all_cities = []
    coordinate_dict = {}
    graph = nx.Graph()
    roads = open(filename1, 'r')
    coordinates = open(filename2, 'r')

    for nodes in roads:
        nodes = nodes.split("(")
        cities = nodes[1].split(",")
        distances = cities[2].split(")")
        city1 = cities[0].strip()
        city2 = cities[1].strip()
        distance = distances[0].strip()
        distance = float(distance)
        graph.add_edge(city1, city2, cost=distance)

    for nodes in coordinates:
        nodes = nodes.split("(")
        city_info = nodes[1].split(",")
        longitudes = city_info[2].split(")")
        city_name = city_info[0].strip()
        latitude = city_info[1].strip()
        longitude = longitudes[0].strip()
        latitude = float(latitude)
        longitude = float(longitude)
        coordinate_dict[city_name] = "%f , %f" % (latitude, longitude)
        all_cities.append(city_name)

    return graph, coordinate_dict, all_cities
