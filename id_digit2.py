from functools import reduce

nums = [123, 789, 300, -44]

total_sum = reduce(lambda acc, num: acc + sum(int(digit) for digit in str(abs(num))), nums, 0)

print(total_sum)