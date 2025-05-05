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

def uniform_cost_search(graph, start, goal, distances):
    visited = set()
    cost_so_far = {start: 0}
    current_node = start
    path = [start]

    while current_node != goal:
        visited.add(current_node)
        neighbors = graph[current_node]
        min_cost = float('inf')
        next_node = None

        for neighbor in neighbors:
            edge_cost = distances.get((current_node, neighbor), distances.get((neighbor, current_node), float('inf')))
            new_cost = cost_so_far[current_node] + edge_cost

            if neighbor not in visited or new_cost < cost_so_far.get(neighbor, float('inf')):
                cost_so_far[neighbor] = new_cost

                if new_cost < min_cost:
                    min_cost = new_cost
                    next_node = neighbor

        if next_node is None:
            return None, float('inf')

        current_node = next_node
        path.append(current_node)

    return path, cost_so_far[goal]

start_node = input("Please enter the start city: ")
goal_node = input("Please enter the goal city: ")

result_path, total_cost = uniform_cost_search(graph, start_node, goal_node, distances)
if result_path:
    print("\nThe Path:", result_path)
    print("Total Distance:", total_cost)
else:
    print("No path found between", start_node, "and", goal_node)
