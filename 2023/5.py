def solve1(seeds, mappings):
    locations = []
    for seed in seeds:
        for mapping in mappings:
            for dest, src, length in mapping:
                if src <= seed < src + length:
                    seed = dest + seed - src
                    break
        locations.append(seed)
    return min(locations)


def solve2(seeds, mappings):
    intervals = []
    min_location = float('inf')
    for start, length in seeds:
        intervals.append([start, start + length - 1, 0])

    while intervals:
        left, right, level = intervals.pop()
        if level == 7:
            min_location = min(min_location, left)
            continue
        
        for dest, src, length in mappings[level]:
            a, b = src, src + length - 1
            if left > b or right < a:
                # no overlap
                continue
            if left < a:
                intervals.append([left, a-1, level])
                left = a
            if right > b:
                intervals.append([b+1, right, level])
                right = b

            diff = dest - src
            intervals.append([left + diff, right + diff, level + 1])
            break
        else:
            # no valid mapping, move to the next level
            intervals.append([left, right, level + 1])
        
    return min_location

segments = open("input.txt", "r").read().strip().split("\n\n")
seeds1 = list(map(int, segments[0].split()[1:]))
mappings = [[list(map(int, line.split())) for line in seg.splitlines()[1:]] for seg in segments[1:]]
print(solve1(seeds1, mappings))

seeds2 = list(zip(map(int, segments[0].split()[1:][0::2]), map(int, segments[0].split()[1:][1::2])))
print(solve2(seeds2, mappings))


'''
  a    b
l    r

  a    b
l         r

  a    b
    l r
    
  a    b
    l    r
'''
