# sum = lambda a,b : a+b
# print(sum(10,29))

glvar1 = "hello"

def funct():
    global var2
    var2 = "aradya"
    print("global var 1 : ",glvar1)
    
funct()
print("inside funct : ",var2)