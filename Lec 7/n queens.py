
n = int(input("Enter the number of queens"))
b = [[0]*n for _ in range(n)]






def att(i, j):
    for k in range(0,n):
        if b[i][k]==1 or b[k][j]==1:
            return True
    for k in range(0,n):
        for z in range(0,n):
            if (k+z==i+j) or (k-z==i-j):
                while(b[k][z]==1):
                    return True
    return False








def NQ(m):
    if m==0:
        return True
    for i in range(0,n):
        for j in range(0,n):
            if (not(att(i,j))) and (b[i][j]!=1):
                b[i][j] = 1
                while(NQ(m-1)==True):
                    return True
                b[i][j] = 0

    return False


NQ(n)

for i in b:
    print(i)

