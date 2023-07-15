def sum_n(n):
    #sum of first n natural nos.
    s = 0
    for i in range(n+1):
        s += i
    return s 
        
n = int(input("enter value for n : "))
print(sum_n(n))