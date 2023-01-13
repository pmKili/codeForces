def preprocess():
    n = int(input())
    shortcuts = input().split(' ')
    shortcuts_int = [int(shortcut) for shortcut in shortcuts]
    return n, shortcuts_int


def get_possible_paths(i, n, shortcuts):
    if i == 1:
        return [[]]
    if i == 2:
        return [[2]]

    dummy_path = [j for j in range(2, i+1)]

    possible_paths = [dummy_path]

    for j in range(i):
        # print(shortcuts[j])
        if shortcuts[j] <= i:
            new_path = [k for k in range(1, j+1)]
            # print(f"newPath1={new_path}")
            new_path = new_path + [k for k in range(shortcuts[j], i+1)]
            # print(f"newPath2={new_path}")

            possible_paths.append(new_path)

    return possible_paths


def find_shortest_paths_weight(possible_paths):
    paths_lengths = [len(path) for path in possible_paths]
    # print(paths_lengths)
    return min(paths_lengths)


def main():
    n, shortcuts = preprocess()

    answer_list = []
    for i in range(1, n+1):
        possible_paths = get_possible_paths(i, n, shortcuts)
        print(possible_paths)

        cost = find_shortest_paths_weight(possible_paths)
        answer_list.append(str(cost))

    answer = ' '.join(answer_list)

    print(answer)


if __name__ == '__main__':
    main()
