def gCd(x, y):
    print ("X = ", x, "Y = ", y)
    if y == 0:  # base case here
        return x
    else:
        return gCd(y, x%y)
        
def main():
    x = 1074
    y = 52
    print("GCD of ", x, ",", y, "=", gCd(x,y))
    
if __name__ == "__main__":
    main()