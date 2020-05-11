def matrix_to_graph(list1):
    global number_of_nodes
    g = {}
    for i in range(number_of_nodes):
        g[i] = {}
    for i in range(number_of_nodes):
        for j in range(number_of_nodes):
            if i != j and list1[i][j] != 0:
                g[i][j] = list1[i][j]
            elif i == j:
                g[i][j] = 9999
    return g


def minimum_spanning_tree():
    global spanning_tree
    different_parts = []
    according_to_weights = [[0, 0, 99999]]
    for i in graph.keys():
        different_parts.append([i])
        spanning_tree[i] = {}
        for j in graph[i].keys():
            for k in range(len(according_to_weights)):
                if graph[i][j] < according_to_weights[k][2] and [j, i, graph[i][j]] not in according_to_weights:
                    according_to_weights.insert(k, [i, j, graph[i][j]])
                    break
    for i in range(len(according_to_weights)):
        for j in range(len(different_parts)):
            if according_to_weights[i][0] in different_parts[j]:
                node_1 = j
            if according_to_weights[i][1] in different_parts[j]:
                node_2 = j
        if node_1 == node_2:
            pass
        else:
            spanning_tree[according_to_weights[i][0]][according_to_weights[i][1]] = graph[according_to_weights[i][0]][
                according_to_weights[i][1]]
            if node_1 > node_2:
                different_parts[node_2] += different_parts[node_1]
                different_parts.pop(node_1)
            else:
                different_parts[node_1] += different_parts[node_2]
                different_parts.pop(node_2)


def print_minimum_spanning_tree(tree):
    for i in tree.keys():
        for j in tree[i].keys():
            print(i, '-->', j, '=', tree[i][j])


print("Enter adjacency matrix")
number_of_nodes = int(input("Enter number of nodes:"))
g = []
for i in range(number_of_nodes):
    g.append([int(x) for x in input().split()])
graph = matrix_to_graph(g)
spanning_tree = {}
minimum_spanning_tree()
print_minimum_spanning_tree(spanning_tree)
