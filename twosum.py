"""
You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""

def two_sum(num_list, target):

    nums_storage = {}

    for i in range(len(num_list)):

        if num_list[i] in nums_storage:
            return [nums_storage[num_list[i]], i]

        else:
            nums_storage[target - num_list[i]] = i

x = [4, 7, 1 , -3, 2]
y = 5

two_sum(x, y)