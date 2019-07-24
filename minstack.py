'''Implement a class for a stack that supports all the regular functions (push, pop)
and an additional function of min()
which returns the minimum element in the stack (return None if the stack is empty).
Each method should run in constant time.'''


class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            mini = self.stack[-1][1]
            self.stack.append((val, min(val, mini)))

    def pop(self):
        self.stack.pop()

    def mini(self):
        return self.stack[-1][1]


test = MinStack()
test.push(3)
test.push(2)
test.push(1)
test.push(0)
print(test.mini())
#0
test.pop()
print(test.mini())
#1