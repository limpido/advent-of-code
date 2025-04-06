from operator import add, mul

inp = open("input.txt").read().strip().splitlines()
lines = [i.split(": ") for i in inp]

calibration_res = []

def operate(nums, index, cur, target):
    if index == len(nums) and cur == target:
        calibration_res.append(target)
        return True
    if cur > target or index == len(nums):
        return False
    cur1 = add(cur, nums[index])
    cur2 = mul(cur, nums[index])
    cur3 = int(str(cur) + str(nums[index]))
    return operate(nums, index + 1, cur1, target) or operate(nums, index + 1, cur2, target) or operate(nums, index + 1, cur3, target)


for line in lines:
    target = int(line[0])
    nums = list(map(int, line[1].split()))
    operate(nums, 1, nums[0], target)

print(sum(calibration_res))