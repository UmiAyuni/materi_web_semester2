# stack implementasi in python (fungsi push)

# creating a stack (buat stack)
def create_stack():
    stack = []
    return stack

# creating an empty stack (memeriksa apa stack kosong)
def check_empty(stack):
    return len(stack) == 0

# adding items into the stack (tambahkanitem pada stack)
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

# Removing an elemet from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

stack = create_stack()
push(stack, 'A')
push(stack, 'B')
push(stack, 'C')
push(stack, 'D')
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
