
def integer(num):
    try:
        return int(num)
    except ValueError as argument:
        print("the value does not contain number\n",argument)
        
integer("hello")
        
