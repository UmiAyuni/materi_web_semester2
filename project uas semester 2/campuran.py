# python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# elemnt in the stuck
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print('Initial stack')
print(stack)

# pop() fuction to pop
# element from stack in
# LIFO order
print('\nelements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an indexError
# as the stack is now empty