di = {0: [1,2,3,4,12],
    1: [0,4,5],
    2: [0,12],
    3: [0,4,12],
    4: [0,3,5,12],
    5: [1,4,6,12],
    6: [5,7],
    7: [5,6,8,12],
    8: [7,9,12],
    9: [8,10,12],
    10: [9,11,12],
    11: [10,12],
    12: [0,2,3,4,5,8,9,10,11]}

countries = ["Argentina", "Chile", "Uruguay", "Paraguay", "Bolivia", "Peru", "Ecuador", "Columbia", "Venezuela", "Guyana", "Suriname", "Guyane", "Brasil"]
c = ["Red", "Green", "Blue", "Yellow"] 

colormap={}
ccount={}


'''
while (a<13):
    colormap.update({a:""})
    a+=1
#for a in range(0,13):
#    colormap.update({a:""})
print(colormap)
'''



def main():
    a=0
    while(a<len(countries)):
        ccount[a]=color(a)
        a+=1
    print(ccount)
#    while(a<len(di)):
#        print(countries[a]+":",+ccount.get(a))
#        a=a+1
    for a in range(0,len(di)):
        print(countries[a]+":",ccount.get(a))



        
def color(a):
    for b in c:
        if check(a,b):
            return b



        
def check(c,d):
    for country in di.get(c): 

        a = ccount.get(country)
 
        if a == d:
            return False
    return True

print(main())      
