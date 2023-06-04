#!/usr/bin/env python

import itertools

def tsp_brute_force(distances, start_city):
    num_cities = len(distances)
    cities = list(range(num_cities))
    cities.remove(start_city)
    min_distance = float('inf')
    best_route = None

    for route in itertools.permutations(cities):
        route = [start_city] + list(route) + [start_city]
        distance = calculate_distance(distances, route)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

def calculate_distance(distances, route):
    distance = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i+1]
        distance += distances[from_city][to_city]
    return distance

# Example usage
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
start_city = 0

best_route, min_distance = tsp_brute_force(distances, start_city)

print("Best route:", best_route)
print("Minimum distance:", min_distance)
