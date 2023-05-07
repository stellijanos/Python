# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def rekursiv(lst,x,start,end):
    if start <=end:
        mid = (start+end) // 2
        if x == lst[mid]:
            return mid
        elif x>lst[mid]:
            return rekursiv(lst,x,mid+1,end)
        else:
            return rekursiv(lst,x,start,mid-1)
    return -1


l=[10,20,30,40,45,50]
print(rekursiv(l,45,0,len(l)-1))