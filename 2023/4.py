def solve1(data):
    res = 0
    winning = [card.split(" | ")[0].split(": ")[1].split() for card in data]
    winning = [set(card) for card in winning]
    yours = [card.split("| ")[1].split() for card in data]

    for i, card in enumerate(yours):
        point = 0
        for n in card:
            if n in winning[i]:
                if point == 0:
                    point = 1
                else: point *= 2
        res += point
    return res


def solve2(data):
    winning = [card.split(" | ")[0].split(": ")[1].split() for card in data]
    winning = [set(card) for card in winning]
    yours = [card.split("| ")[1].split() for card in data]
    instances = [1] * len(yours)
    
    for idx, cards in enumerate(yours):
        match = 0
        for num in cards:
            if num in winning[idx]:
                match += 1
        for j in range(idx+1, idx+match+1):
            instances[j] += instances[idx]
    return sum(instances)


filename = 'input.txt'
with open(filename, 'r') as f:
    data = f.read().strip().splitlines()
    print(solve1(data))
    print(solve2(data))