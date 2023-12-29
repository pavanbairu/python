a = 10
b = 20

def addition():
    add = a+b
    print("addition", add)

def subtraction():
    sub = a-b
    print("subtraction", sub)

def multiplication():
    mul = a*b
    print("multiplication", mul)

addition()
subtraction()
multiplication()

# accepting the arguments as input instead of fixed values
def add(n1, n2):
    sum = n1 + n2
    return sum

# calling the function by passing the inputs dynamically
x = add(30, 90)

print(x)

print(add(40, 60))
