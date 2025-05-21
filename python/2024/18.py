data = [*map(eval, open("../inp.txt"))]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def steps(num_bytes):
    visited = {*data[:num_bytes]}
    queue = [(0, (0, 0))]
    while len(queue) > 0:
        step, (r, c) = queue.pop(0)
        if (r, c) == (70, 70):
            return step

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and 0 <= nr <= 70 and 0 <= nc <= 70:
                queue.append((step + 1, (nr, nc)))
                visited.add((nr, nc))
    return float("inf")


print(steps(1024))
for i in range(1025, len(data)):
    if steps(i) == float("inf"):
        print(data[i - 1])
        break
