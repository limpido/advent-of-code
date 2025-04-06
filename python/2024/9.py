inp = list(map(int, open("input.txt").read().strip()))

blocks = []
block_id = 0
for i in range(0, len(inp), 2):
    file_size = inp[i]
    blocks.extend([block_id] * int(file_size))
    block_id += 1
    if i != len(inp) - 1:
        free_size = inp[i + 1]
        blocks.extend(["."] * int(free_size))


def part1(blocks):
    checksum = 0
    l, r = 0, len(blocks) - 1
    while l <= r:
        if blocks[l] == ".":
            blocks[l], blocks[r] = blocks[r], blocks[l]
            while blocks[r] == ".":
                r -= 1
        checksum += blocks[l] * l
        l += 1
    print(checksum)


def checksum(file_id, position, block_nr):
    checksum = 0
    for i in range(block_nr):
        checksum += file_id * (position + i)
    return checksum


def part2(inp):
    modifiable_inp = inp[:]
    res = 0
    for l in range(len(inp)):
        if l % 2 == 0 and modifiable_inp[l] != 0:
            res += checksum(l // 2, sum(inp[:l]), inp[l])
            continue
        free = inp[l]
        pos_offset = 0
        while free > 0:
            found = False
            for r in range(len(inp) - 1, l, -2):
                if modifiable_inp[r] == 0 or modifiable_inp[r] > free:
                    continue
                found = True
                res += checksum(r // 2, sum(inp[:l]) + pos_offset, inp[r])
                free -= inp[r]
                pos_offset += inp[r]
                modifiable_inp[r] = 0
            if not found:
                break
    print(res)


part1(blocks[:])
part2(inp)
