



include = [0,0,0]


def promising (i, weight, profit, n, W, w, p):
    #j k
    #totweight
    #float bound
    j = 0
    k = 0
    
    if (weight >= W):                           
        return False                  
    else:                                 
        j = i + 1                              
        bound = profit                         
        totweight = weight
        while ((j <= n) and (totweight + w[j] <= W)):
            totweight = totweight + w[j]               
            bound = bound + p[j]
            j = j + 1
            
        k = j                                 
        if k<=n:                              
            bound = bound + (W - totweight) * p[k]/w[k]

        return bound > maxprofit                           
   


numbest = 0
maxprofit = 0
def knapSackBackTracking(i, profit, weight, W, maxprofit, n, w, p):
    if weight <= W and profit > maxprofit:
        maxprofit = profit                  #   so far.
        #bestset = include
    if promising(i,weight, profit, n, W, w, p):
         #include[i + 1] = "yes"            
         knapSackBackTracking(i + 1, profit + p[i + 1], weight + w[i + 1], maxprofit, n, w, p)
         #include[i + 1] = "no"              
         knapSackBackTracking(i + 1, profit, weight,maxprofit, maxprofit, n, w, p)
    return maxprofit

print("Backtracking:")



p = [60, 100, 120]
w = [10, 20, 30]
W = 50
n = len(p)
print( knapSackBackTracking(0, 0, 0, W, 0, n, w, p) )

# for j in numbest:                           #   Show an optimal set of items.
#     print(bestset[j])

