rules, pages = open("input.txt").read().split("\n\n")
rules = [rule.split("|") for rule in rules.splitlines()]
pages = [p.split(",") for p in pages.splitlines()]


# Bubble Sort
## Part 1
def bubbleSort1(page):
    for i in range(len(page)):
        for j in range(len(page) - 1 - i):
            if [page[j + 1], page[j]] in rules:
                return 0

    mid = len(page) // 2
    return int(page[mid])

print(sum(map(bubbleSort1, pages)))


## Part 2
def bubbleSort2(page):
    incorrect = False
    for i in range(len(page)):
        for j in range(len(page) - 1 - i):
            if [page[j + 1], page[j]] in rules:
                incorrect = True
                page[j], page[j + 1] = page[j + 1], page[j]
    if incorrect:
        mid = len(page) // 2
        return int(page[mid])
    return 0

print(sum(map(bubbleSort2, pages)))


# TODO: Topological Sort
