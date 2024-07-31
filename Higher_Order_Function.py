
# A function take values from anothe function is called higher order function

def apply_operation(operation, x, y):
    return operation(x, y)

# Example usage:
def add(x, y):
    return x + y

result = apply_operation(add, 3, 4)
print("Result of addition:", result)

def sum(addition, a, b):
    return  addition (a, b)

def total(a,b):
    return  a+b
resu = sum(total,10,20)
print(resu)

def multiplication(multiply, k, l):
    return  multiply(k,l)

def sum_of(k,l):
    return k*l
result1 = multiplication(sum_of,2,5)
print("Multipication of two num: ", result1)