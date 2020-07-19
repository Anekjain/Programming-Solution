
def DPFib(n,memo):
    if(memo[n] != None):
        return memo[n]
    if(n==1 or n==2):
        result = 1
        memo[n] = result
        return result
    else:
        result = DPFib(n-1,memo)+DPFib(n-2,memo)
        memo[n] = result
        return result

def fib(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__=="__main__":
    n = 30
    memo = [None] * (n+1)
    r = DPFib(n, memo)
    # r = fib(n)
    print(r)

