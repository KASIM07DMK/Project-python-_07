import math
def is_Prime(n):
    if(n<=1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return True
        return False
        num = 29
        if(is_Prime(num)):
            print("Prime")
        else:
             print("True")

