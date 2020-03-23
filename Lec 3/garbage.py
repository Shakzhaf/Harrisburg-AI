def bs(list,num):    

    mid=int(len(list)/2)        
    if num==list[mid]:
         return mid
    if len(list)==1:
       return -1

    elif num<list[mid]:           
        return bs(list[0:mid],num)    
    elif num>list[mid]:           
        return bs(list[mid:],num)
list=[1,2,3,4,5,6,7,8,9,10]
print(bs(list,4))
https://rosettacode.org/wiki/Binary_search
