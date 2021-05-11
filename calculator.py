def add(num):
    result = 0
    for i in num:
        result += i
    return result

def sub(num):
    result = 0
    for i in num:
        result -= i
    return result

def mult(num):
    result = 1
    for i in num:
        result *= i
    return result

def div(num):
    result = 1
    for i in num:
        result /=  i
    return result

print("\nadd -> Addition\nsub -> Subrection\nmult -> Multiply\ndiv -> Devision\n")    #Initalyzing the operator
op = input("Enter the above operation you want to performe: ")

x = [int(x) for x in input("Enter the numbers to perform the operation with spaces value: ").split()]            #Initalyzing the variable

if op.upper() == 'MULT':
    print(mult(x))
elif op.upper() == 'ADD':
    print(add(x))
elif op.upper() == 'SUB':
    print(sub(x))
elif op.upper() == 'DIV':
    print(div(x))
else:
    print("The operation is not posible in this calculator")