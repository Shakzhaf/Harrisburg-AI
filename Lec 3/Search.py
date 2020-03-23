f = open("data.csv", "r")
z = open("data2.csv", "r")
f1=f.readlines()
z1=z.readlines()
f1[0]=f1[0][3:]
z1[0]=z1[0][3:]
o=z1[0].split(',')
print(o)


print("THIS IS ITERATIVE LINEAR SEARCH")
def IterativeLinear(t, m):
    l=f1[t].split(',')
    for i in range (len(l)):
        if (int(l[i]) == m):
            return i
    return -1
print(IterativeLinear(0,42))


print("THIS IS RECURSIVE LINEAR SEARCH")
def RecursiveLinear(t, m):
    l=f1[t].split(',')
#    print (l)
    ret = helpsearch(l,m,0)
    if (int(l[ret]) == m):
        return ret
    else:
        return -1
    

def helpsearch(t,m,i):
    if (int(t[i])==m):
        return i
    else:    
        return helpsearch(t,m,i+1)
print(RecursiveLinear(0,42))







print("THIS IS ITERATIVE BINARY SEARCH")
def IterativeBinary(t,n):
    low=0
    high=int(len(t)-1)
    while(int(low)<=int(high)):
        mid=(low+high)//2
        if(int(t[mid])>n):
            high=mid-1
        elif(int(t[mid])<int(n)):
            low=mid+1
        else:
            return mid
    else:
        return -1

print(IterativeBinary(o,96))




print("THIS IS RECURSIVE BINARY SEARCH")
def RecursiveBinary(t,m):
    low = 0
    high = len(t)-1
    rr = helpbinary(t, m, low, high)
    return rr
    
def helpbinary(t, m, low, high):
    mid = (low+high) // 2
    if m == int(t[mid]):
        return mid
    elif m < int(t[mid]):
        return helpbinary(t,m,low,mid-1)
    elif m > int(t[mid]):
        return helpbinary(t,m,mid+1,high)
    else:
        return -1

print(RecursiveBinary(o,53))



#Attempted question no.11. but there are errors i cant understand. Guess the syntax is wrong
'''

def binary_search(x, lst, low=None, high=None) :
    start:
        low = 0
        high = len(lst)-1
        mid = low + (high - low) // 2
        if low > high :
            return None
    elif lst[mid] == x :
        return mid
    elif lst[mid] > x :
        (x, lst, low, high) = (x, lst, low, mid-1)
        goto start
    else :
        (x, lst, low, high) = (x, lst, mid+1, high)
        goto start

print(binary_search(o,96,0, int(len(t)-1))
'''
