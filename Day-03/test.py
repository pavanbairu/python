print("pavan")

a  = 10
b  = 20

print(a+b)


def add():
    # local variables access with in the function itself
    c = 10
    d = 20
    print(c+d)

def mul():
    # c and d are local variables and cannot be accessed here
    print(c*d)

add()
mul()
