stack = []

def push(value):
    stack.append(value)

def pop():
    stack.pop()

def noel():
    print (len(stack))

def top():
    top = len(stack) - 1
    if top < 0:
        print ("tidak terdefinisikan")
    else:
        print (stack[top])

def isempty():
    if len(stack) == 0:
        print ("True")
    else:
        print ("False")

def tampilkan(stack):
    print(stack)

while True:
    value = input("--> ")