def preprocess():
    n = int(input())
    shortcuts = input().split(' ')
    shortcuts_int = [int(shortcut) for shortcut in shortcuts]
    return n, shortcuts_int


def get_column_i(i, n, shortcuts):
    shortcut = shortcuts[i]
    column = [0 for i in range(n)]
    column[i+1] = 1
    column[shortcut] = 1


def get_adjacency_matrix(n, shortcuts):
    matrix = []

    for i in range(n):
        matrix.append(get_column_i(i, n, shortcuts))

    return matrix


def get_shortest_path(i, A, n):
    visited = [False] * n
    visited[0] = True

    cost = 0

    queue = []
    for intersection in A[0]:
        if intersection == 1:
            queue.append((intersection, cost))

    while queue:
        intersection = queue.pop(0)
        visited[intersection] = True
        for neighbors in A[intersection]:
            if neighbors == 1 and not visited[neighbors]:
                queue.append(neighbors)


def main():
    n, shortcuts = preprocess()

    A = get_adjacency_matrix(n, shortcuts)
