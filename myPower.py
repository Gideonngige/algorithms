def myPow(x: float, n: int) -> float:
    def myPowHelper(x, n):
        #Base case 
        if n == 0:
            return 1 
        #calculate for half of the exponent 
        half = myPowHelper(x, n//2)

        if n%2 == 0:
            return half * half 
        else:
            return half * half * x 
    #handle negattive exponent
    if n < 0:
        return 1 / myPowHelper(x, -n)
    return myPowHelper(x, n)

x = 2
n = 10
print(myPow(x, n))