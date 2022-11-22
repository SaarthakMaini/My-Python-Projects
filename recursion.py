L=[0,11,12,16,2,3,4,5,6]
#check for 0

def checkO(L):
    print(L)
    if len(L)==0:
        return False
    if L[0]==0:
        return True
    L.pop(0)
    print(L)
    return checkO(L)

print(checkO(L))    
