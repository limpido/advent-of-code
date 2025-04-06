rounds = [r.split(" ") for r in open("input.txt").read().splitlines()]

score = [3, 6, 0]
char_diff = lambda char1, char2: ord(char1) - ord(char2)
get_score = lambda other, me: score[char_diff(me, "X") - char_diff(other, "A")] + char_diff(me, "X") + 1

res = 0
for other, me in rounds:
    res += get_score(other, me)
print(res)


res = 0
score = [0, 3, 6]
choices = "ABC"
for other, result in rounds:
    res += score[char_diff(result, "X")]
    me = choices[(choices.index(other) + char_diff(result, "X") - 1) % 3]
    res += char_diff(me, "A") + 1
print(res)
