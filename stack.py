class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Current stack:", stack.items)
print("Size of stack:", stack.size())
print("Top of stack:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Updated stack:", stack.items)
