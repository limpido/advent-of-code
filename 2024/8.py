board = [r for r in open("input.txt").read().splitlines()]
ROW, COL = len(board), len(board[0])

all_antennas = {}
antinodes = set()

def within_border(r, c):
    return 0 <= r < ROW and 0 <= c < COL

# collect antennas by frequency
for r in range(ROW):
    for c in range(COL):
        if board[r][c] == ".":
            continue
        freq = board[r][c]
        if freq not in all_antennas:
            all_antennas[freq] = []
        all_antennas[freq].append((r, c))

for freq, locs in all_antennas.items():
    for i in range(len(locs)):
        antinodes.add(tuple(locs[i]))
        r0, c0 = locs[i]
        for j in range(i+1, len(locs)):
            r1, c1 = locs[j]
            
            # calculate the distance between any two antenna on same frequency
            dr = r0 - r1
            dc = c0 - c1

            # calculate antinode locations
            ant1 = (r0 + dr, c0 + dc)
            while within_border(*ant1):
                antinodes.add(ant1)
                ant1 = (ant1[0] + dr, ant1[1] + dc)

            ant2 = (r1 - dr, c1 - dc)
            while within_border(*ant2):
                antinodes.add(ant2)
                ant2 = (ant2[0] - dr, ant2[1] - dc)

print(len(antinodes))
