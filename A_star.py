graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Sibiu': ['Arad', 'Fagaras', 'Rimnicu_Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu_Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Urziceni', 'Giurgiu'],
    'Pitesti': ['Rimnicu_Vilcea', 'Bucharest', 'Craiova'],
    'Craiova': ['Rimnicu_Vilcea', 'Pitesti', 'Dobreta'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Giurgiu': ['Bucharest'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Eforie': ['Hirsova'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

heuristic = {
    'Arad': 366, 'Zerind': 374, 'Sibiu': 253, 'Timisoara': 329, 'Oradea': 380,
    'Fagaras': 178, 'Rimnicu_Vilcea': 193, 'Lugoj': 244, 'Bucharest': 0,
    'Pitesti': 98, 'Craiova': 160, 'Mehadia': 241, 'Urziceni': 80,
    'Giurgiu': 77, 'Dobreta': 242, 'Hirsova': 151, 'Vaslui': 199,
    'Eforie': 161, 'Iasi': 226, 'Neamt': 234
}

distances = {
    ('Arad', 'Zerind'): 75, ('Arad', 'Sibiu'): 140, ('Arad', 'Timisoara'): 118,
    ('Zerind', 'Oradea'): 71, ('Sibiu', 'Fagaras'): 99, ('Sibiu', 'Rimnicu_Vilcea'): 80,
    ('Timisoara', 'Lugoj'): 111, ('Oradea', 'Sibiu'): 151, ('Fagaras', 'Bucharest'): 211,
    ('Rimnicu_Vilcea', 'Pitesti'): 97, ('Rimnicu_Vilcea', 'Craiova'): 146,
    ('Lugoj', 'Mehadia'): 70, ('Bucharest', 'Pitesti'): 101, ('Bucharest', 'Urziceni'): 85,
    ('Pitesti', 'Craiova'): 138, ('Mehadia', 'Dobreta'): 75, ('Urziceni', 'Hirsova'): 98,
    ('Urziceni', 'Vaslui'): 142, ('Giurgiu', 'Bucharest'): 90, ('Dobreta', 'Craiova'): 120,
    ('Hirsova', 'Eforie'): 86, ('Vaslui', 'Iasi'): 92, ('Iasi', 'Neamt'): 87
}

def check_heuristic_admissibility(graph, distances, heuristic):
    for node in graph:
        for neighbor in graph[node]:
            actual_distance = distances.get((node, neighbor), distances.get((neighbor, node), float('inf')))
            if heuristic[node] > heuristic[neighbor] + actual_distance:
                return False
    return True

def a_star_search(graph, start, goal, heuristic, distances):
    visited = set()
    open_list = [(start, 0, heuristic[start], [start])]
    while open_list:
        open_list.sort(key=lambda x: x[2])
        current_node, g, _, path = open_list.pop(0)
        if current_node == goal:
            return path, g
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                actual_distance = distances.get((current_node, neighbor), distances.get((neighbor, current_node), float('inf')))
                new_g = g + actual_distance
                new_f = new_g + heuristic[neighbor]
                open_list.append((neighbor, new_g, new_f, path + [neighbor]))
    return None, float('inf')

start_node = input("Please enter the start city: ")
goal_node = input("Please enter the goal city: ")
print()

if check_heuristic_admissibility(graph, distances, heuristic):
    print("The heuristic is admissible. Running A* search...\n")
    result, total_distance = a_star_search(graph, start_node, goal_node, heuristic, distances)
    if result:
        print("The Path:", " -> ".join(result))
        print("Total Distance:", total_distance)
    else:
        print(f"No path found from {start_node} to {goal_node}.")
else:
    print("The heuristic is not admissible. Terminating.")
