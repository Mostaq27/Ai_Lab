graph = {
    'Arad': ['Zerind','Sibiu','Timisoara'],
    'Zerind': ['Arad','Oradea'],
    'Sibiu': ['Arad','Fagaras','Rimnicu_Vilcea'],
    'Timisoara': ['Arad','Lugoj'],
    'Oradea': ['Zerind','Sibiu'],
    'Fagaras': ['Sibiu','Bucharest'],
    'Rimnicu_Vilcea': ['Sibiu','Pitesti','Craiova'],
    'Lugoj': ['Timisoara','Mehadia'],
    'Bucharest': ['Fagaras','Pitesti','Urziceni','Giurgiu'],
    'Pitesti': ['Rimnicu_Vilcea','Bucharest','Craiova'],
    'Craiova': ['Rimnicu_Vilcea','Pitesti','Dobreta'],
    'Mehadia': ['Lugoj','Dobreta'],
    'Urziceni': ['Bucharest','Hirsova','Vaslui'],
    'Giurgiu': ['Bucharest'],
    'Dobreta': ['Mehadia','Craiova'],
    'Hirsova': ['Urziceni','Eforie'],
    'Vaslui': ['Urziceni','Iasi'],
    'Eforie': ['Hirsova'],
    'Iasi': ['Vaslui','Neamt'],
    'Neamt': ['Iasi']
}

heuristic = {
    'Arad': 366, 'Zerind': 374, 'Sibiu': 253, 'Timisoara': 329, 'Oradea': 380,
    'Fagaras': 178, 'Rimnicu_Vilcea': 193, 'Lugoj': 244, 'Bucharest': 0,
    'Pitesti': 98, 'Craiova': 160, 'Mehadia': 241, 'Urziceni': 80, 'Giurgiu': 77,
    'Dobreta': 242, 'Hirsova': 151, 'Vaslui': 199, 'Eforie': 161, 'Iasi': 226, 'Neamt': 234
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

def greedy_best_first_search(graph, start, goal, heuristic, distances):
    visited = []
    current_node = start
    total_distance = 0
    while current_node != goal:
        visited.append(current_node)
        neighbours = graph[current_node]
        neighbours = sorted(neighbours, key=lambda node: heuristic[node])
        for neighbour in neighbours:
            if neighbour not in visited:
                if (current_node, neighbour) in distances:
                    total_distance += distances[(current_node, neighbour)]
                elif (neighbour, current_node) in distances:
                    total_distance += distances[(neighbour, current_node)]
                current_node = neighbour
                break
    visited.append(goal)
    return visited, total_distance

start_node = input("Please enter the start city: ")
goal_node = input("Please enter the goal city: ")
print("\n")
result, total_distance = greedy_best_first_search(graph, start_node, goal_node, heuristic, distances)
print("The Path:", result)
print("Total Distance:", total_distance)
