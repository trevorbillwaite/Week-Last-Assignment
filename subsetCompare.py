import math
import time
def subsetI(n,k):
    return math.factorial(n) / (math.factorial(k)* math.factorial(n-k))

def subsetR(n,k):
    if ????		#base case 1
        return ??
    if ?????	#base case 2
        return ??
    else:
        return ????????  #recursion


def main():
    n = 20
    k = 5

    timeB = time.time()
    for x in range(1000):
        I = subsetI(n,k)
    timeA = time.time()
    print("I = ",I)
    print("elapsed time: ", timeA-timeB)

    timeB = time.time()
    for x in range(1000):
        R = subsetR(n,k)    
    timeA = time.time()
    print("R = ",R)
    print("elapsed time: ", timeA-timeB)
 

    
