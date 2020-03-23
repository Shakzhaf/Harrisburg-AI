z = open("data2.csv", "r")
f1=f.readlines()
z1=z.readlines()
f1[0]=f1[0][3:]
z1[0]=z1[0][3:]
o=z1[0].split(',')
print(o)

'''
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
