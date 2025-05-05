def alphabeta(depth, node, alpha, beta, maximizing_player, node_values, tree_structure, height):
    if depth == height:
        print(f"Visited leaf node: {node} with value: {node_values[node]}")
        return node_values[node]

    if maximizing_player:
        max_value = float('-inf')
        for child in tree_structure[node]:
            print(f"Maximizing: Visiting node {node}, exploring child {child}")
            value = alphabeta(depth + 1, child, alpha, beta, False, node_values, tree_structure, height)
            max_value = max(max_value, value)
            alpha = max(alpha, max_value)
            if beta <= alpha:
                print(f"Maximizing: Pruning at node {node} with alpha: {alpha}, beta: {beta}")
                break
        print(f"Maximizing: Node {node} returns value: {max_value}")
        return max_value
    else:
        min_value = float('inf')
        for child in tree_structure[node]:
            print(f"Minimizing: Visiting node {node}, exploring child {child}")
            value = alphabeta(depth + 1, child, alpha, beta, True, node_values, tree_structure, height)
            min_value = min(min_value, value)
            beta = min(beta, min_value)
            if beta <= alpha:
                print(f"Minimizing: Pruning at node {node} with alpha: {alpha}, beta: {beta}")
                break
        print(f"Minimizing: Node {node} returns value: {min_value}")
        return min_value

node_values = {
    'c': 10, 'd': 6, 'f': 100, 'g': 8,
    'j': 1, 'k': 2, 'm': 20, 'n': 4
}

tree_structure = {
    'z': ['a', 'h'],
    'a': ['b', 'e'],
    'h': ['i', 'l'],
    'b': ['c', 'd'],
    'e': ['f', 'g'],
    'i': ['j', 'k'],
    'l': ['m', 'n']
}

tree_height = 3

optimal_value_alpha_beta = alphabeta(0, 'z', float('-inf'), float('inf'), True, node_values, tree_structure, tree_height)

print("\nOptimal value using Alpha-Beta Pruning:", optimal_value_alpha_beta)
