# Problem
# Design a stack data structure that supports standard stack operations while also being able to retrieve the minimum element in the stack in constant time O(1).

# Definition
# Implement a class called MinStack with the following methods:
# MinStack()
# Initializes an empty stack object.
# push(int val)
# Pushes the element val onto the top of the stack.
# pop()
# Removes the element on the top of the stack.
# top()
# Returns the value of the element on the top of the stack.
# getMin()
# Returns the minimum element currently present in the stack.

# Note
# All operations must run in O(1) time complexity.
# The stack must correctly track the minimum value after each push and pop operation.
# Built-in operations for pushing and popping elements are allowed, but the minimum value must not be recomputed by scanning the stack.

# Return
# top() returns an integer representing the top element of the stack.
# getMin() returns an integer representing the minimum element in the stack.
# push() and pop() do not return any value.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
          self.min_stack.append(val)
        else:
            if val < self.min_stack[-1]:
              self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.push(0)
    minStack.push(2)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
