# creating a stack
def create_stack():
    stack = []
    return stack

# creating an empty stack
def is_empty(stack):
    return len(stack) == 0

# adding an item into stack
def push(stack, item):
    stack.append(item)
    print("Pushed item = " + item)

# removing an item from stack
def pop(stack):
    if (is_empty(stack)):
        print("Empty stack")

    return stack.pop

stack = create_stack()
push(stack, str(1))
push(stack, str(4))
push(stack, str(3))
push(stack, str(1))
print("Popped item" + pop(stack))
print("Stack after popping an element" + (stack))
