
def knapsack(wt, val, W, n):

    #BASE CONDITION
    if(n==0 or W == 0):
        return 0

    #LOGIC
    for i in range(n,0,-1):
        if(wt[i-1]<=W):
            return max(val[i-1] + knapsack(wt, val, W-wt[i-1], n-1), knapsack(wt, val, W, n-1))
        elif(wt[i-1]>W):
            return knapsack(wt, val, W, n-1)


if __name__=="__main__":
    wt = [1,2,4,1]
    val = [1,5,2,1]
    W = 10
    n = len(wt)
    max_profit = knapsack(wt, val, W, n)
    print(max_profit)
