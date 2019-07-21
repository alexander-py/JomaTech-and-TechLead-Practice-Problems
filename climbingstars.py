"""
70 Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):

    def climbing_stairs(self, n):

        steps = [0 for i in range(n+1)]

        for numbers in (0, 1, 2):
            steps[numbers] = numbers

        for numbers in range(3, n+1):
            steps[numbers] = steps[numbers - 1] + steps[numbers - 2]

        return steps[n]

obj = Solution()
test = obj.climbing_stairs(5)
print(test)