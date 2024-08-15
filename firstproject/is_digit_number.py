def sum_digit(nums):
    total_sum = 0


    for num in nums:
        for digit in str(abs(num)):
            total_sum += int(digit)

    return total_sum
"""
Выводит сумму цифр в заданных списком чисел
"""

nums = [123, 789, 300, -44]
print(sum_digit(nums))  #41