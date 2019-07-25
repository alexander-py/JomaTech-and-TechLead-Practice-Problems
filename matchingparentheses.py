"""
Imagine you are building a compiler.
Before running any code, the compiler must check that the parentheses in the program are balanced.
Every opening bracket must have a corresponding closing bracket.
We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""

class Solution(object):

    def checker(self, x):

        stack = []
        open_brackets = ["[", "{", "("]
        close_brackets = ["]", "}", ")"]

        for i in x:
            if i in open_brackets:
                stack.append(i)
            elif i in close_brackets:
                position = close_brackets.index(i)
                if (len(stack)) and (open_brackets[position] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True

tesla = Solution()
string1 = "((()))"
string2 = "[()]{}"
string3 = "({[)]"
print(string1, "-", tesla.checker(string1))
print(string2, "-", tesla.checker(string2))
print(string3, "-", tesla.checker(string3))
