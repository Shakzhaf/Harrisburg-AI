def binary_search(x, lst, low=None, high=None) :
  start:
    if low == None : low = 0
    if high == None : high = len(lst)-1
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
