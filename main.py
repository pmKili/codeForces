import networkx as nx


def preprocess():
    n = int(input())
    shortcuts = input().split(' ')
    shortcuts_int = [int(shortcut) for shortcut in shortcuts]
    return n, shortcuts_int


def get_shortest_path(i):
    if i == 0:
        return []


def create_graph(n):
    G = nx.DiGraph()
    for i in range(1, n+1):
        G.add_node(i)

    for i in range(1, n+1):
        for j in range(1, n+1):
            G.add_edge(i, j, weight=abs(i-j))

    return G


def get_path_cost(G, path):
    path_length = len(path)
    if path_length == 0:
        return 0

    cost = 0
    for i in range(0, path_length - 1):
        u = path[i]
        v = path[i+1]
        cost += G[u][v]['weight']

    return cost


def main():
    n, shortcuts = preprocess()

    G = create_graph(n)
    answer_list = []
    for i in range(1, n+1):
        path = nx.shortest_path(G, source=1, target=i)
        cost = get_path_cost(G, path)
        answer_list.append(str(cost))

    answer = ' '.join(answer_list)

    print(answer)


if __name__ == '__main__':
    main()
