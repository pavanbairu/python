import sys # importing sys module for the runtime arguments

def add(n1, n2):    
    sum = n1 + n2
    return sum

def sub(n1, n2):
    subtraction = n1 - n2
    return subtraction

def mul(n1, n2):
    multiplication = n1 * n2
    return multiplication

# passing the input from command line in runtime
operation = sys.argv[1]    
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])

if operation == "add":
    output = add(n1, n2)
    print("add : ",output)

if operation == "mul":
    output = mul(n1, n2)
    print("mul : ",output)

if operation == "sub":
    output = sub(n1, n2)
    print("sub :", output)