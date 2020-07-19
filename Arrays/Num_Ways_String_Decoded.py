def num_ways_dp(data):
    
    memo = [0] * (len(data)+1)
    helper(data,len(data),memo)

def helper(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] != 0:
        return memo[k]
    result = helper(data,k-1,memo)
    if k>=2 and int(data[s:s+2]) <=26:
        result += helper(data,k-2,memo)
        memo[k] = result
        return result

if __name__=="__main__":
    data = input("Enter a String to Get Number of ways it can be Decoded ?")
    print(num_ways_dp(data))
