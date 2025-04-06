from operator import mul
from functools import reduce

data = [line.split() for line in open("input.txt").read().splitlines()]
hand = [d[0] for d in data]
bid = {d[0]: int(d[1]) for d in data}


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.count = self.count_hand()
        self.product = reduce(mul, self.count)

    def __lt__(self, other):
        if max(self.count) != max(other.count):
            return max(self.count) < max(other.count)
        if self.product != other.product:
            return self.product < other.product
        for i in range(len(self.hand)):
            if self.hand[i] == other.hand[i]:
                continue
            return STRENGTH.index(self.hand[i]) > STRENGTH.index(other.hand[i])

    def count_hand(self):
        if USE_JOKER:
            count = []
            count_J = 0
            for c in set(self.hand):
                if c == "J":
                    count_J = self.hand.count(c)
                else:
                    count.append(self.hand.count(c))
            if len(count):
                i = count.index(max(count))
                count[i] += count_J
            else:  # for case JJJJJ
                count.append(count_J)
            return count
        else:
            return [self.hand.count(c) for c in set(self.hand)]


for USE_JOKER in (False, True):
    STRENGTH = "AKQT98765432J" if USE_JOKER else "AKQJT98765432"
    hand_objs = list(map(Hand, hand))
    print(sum([mul(bid[h.hand], (i + 1)) for i, h in enumerate(sorted(hand_objs))]))
