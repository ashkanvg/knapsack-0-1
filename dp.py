from timeit import default_timer


def knapSackDP(W, wt, pi, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)] # dp[n][w]
  
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(pi[i-1] + dp[i-1][w-wt[i-1]],  dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
  
    return dp[n][W]


# main:
# pi = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50


# EX1:
pi = [12, 2, 2, 10, 1]
wt = [4, 2, 1, 4, 1]
W = 15

# EX2: 
# pi = [40, 100, 50, 60, 10]
# wt = [20, 10, 40, 30, 5]
# W = 60

# EX3: 
# pi = [505, 352, 458, 220, 354]
# wt = [23, 26, 20, 18, 32]
# W = 67

# EX4:
# pi = [414, 498, 545, 473, 543]
# wt = [27, 29, 26, 30, 27]
# W = 67

# EX5:
# pi = [20, 10, 40, 15, 25]
# wt = [1, 3, 8, 7, 4]
# W = 10



n = len(pi)

print("Dynamic Programming:")

start = default_timer()
print(knapSackDP(W, wt, pi, n))
end = default_timer()
print(end-start)
  

