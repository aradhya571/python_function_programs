# Write a program using user defined function that accepts an integer
# and increments the value by 5. Also display the id of argument (before function call),
# id of parameter before increment and after increment

def accept(a):
    print(id(a))
    a += 5
    print(id(a))
    return a

a = int(input("enter value for a : "))
print(id(a))
print(accept(a))