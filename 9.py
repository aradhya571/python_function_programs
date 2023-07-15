def rev_str(str,n):
    rev = ""
    while n :
        rev += str[n-1]
        n -= 1
    return rev
str = input("enter string : ")
n = len(str)
print("rev : ",rev_str(str,n))