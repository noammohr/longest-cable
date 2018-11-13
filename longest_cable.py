# Given a map of cities connected with each other via cable lines such that
# there is no cycle between any two cities, returns the maximum length of
# cable between any two cities.
#
# Arguments:
#   graph (list of list) - adjacency matrix where each index represents a
#     city and the values represent the length of cable connecting them.
# Returns:
#   float - longest distance of cable between any two cities.
def longest_cable(graph):
    start = 0 # Arbitrary starting node.
    farthest_city, farthest_distance = _find_farthest_city(start, graph)
    farthest_city, farthest_distance = _find_farthest_city(farthest_city, graph)
    return farthest_distance

# Find the farthest city from a given city in the graph, and its distance.
#
# Arguments:
#   city (int) - index representing the city in the graph from which to find
#     the farthest city from it.
#   graph (list of list) - adjacency matrix where each index represents a
#     city and the values represent the length of cable connecting them.
# Returns:
#   (int, float) - index representing farthest city, and the length of cable
#     between city and this farthest city.
def _find_farthest_city(city, graph):
    # Total cable lengths from city to each other city.
    distances = _get_distances(city, graph)
    
    # Find longest cable from city.
    max_distance = -float("inf")
    for other_city, distance in enumerate(distances):
        if distance > max_distance:
            max_distance = distance
            farthest_city = other_city
    return farthest_city, max_distance

# Perform a depth first search to determine distances from city to every other
# city.
#
# Arguments:
#   city (int) - index representing the starting city in the depth first search.
#   graph (list of list) - adjacency matrix where each index represents a
#     city and the values represent the length of cable connecting them.
# Returns:
#   list of float - distance to each city from starting city.
def _get_distances(city, graph, visited, distances):
    def _depth_first_search(city, graph, visited, distances):
        visited[city] = True
        for next_city, next_distance in enumerate(graph[city]):
            if next_distance is not None and not visited[next_city]:
                distances[next_city] = distances[city] + graph[city][next_city]
                _depth_first_search(next_city, graph, visited, distances)

    distances = [-float("inf")] * len(graph)
    visited = [False] * len(graph)
    distances[city] = 0
    _depth_first_search(city, graph, visited, distances)
    return distances
