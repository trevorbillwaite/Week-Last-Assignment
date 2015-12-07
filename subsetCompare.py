import math
import time
def subsetI(n,k):
    return math.factorial(n) / (math.factorial(k)* math.factorial(n-k))

def subsetR(n,k):
    if n == k:		#base case 1
        return 1
    if k == 0:	#base case 2
        return 1
    else:
        return subsetR(n-1, k-1) + subsetR(n-1, k)  #recursion


def main():
    n = 52
    k = 13
    looptime = 1

    timeB = time.time()
    for x in range(looptime):
        I = subsetI(n,k)
    timeA = time.time()
    print("I = ",I)
    print("elapsed time: ", timeA-timeB)

    timeB = time.time()
    for x in range(looptime):
        R = subsetR(n,k)    
    timeA = time.time()
    print("R = ",R)
    print("elapsed time: ", timeA-timeB)
 
if __name__ == "__main__":
    main()

    
