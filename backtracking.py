from timeit import default_timer

# EX1:
# p = [12, 2, 2, 10, 1]
# w = [4, 2, 1, 4, 1]
# W = 15

# EX2: 
# p = [40, 100, 50, 60, 10]
# w = [20, 10, 40, 30, 5]
# W = 60

# EX3: 
# p = [505, 352, 458, 220, 354]
# w = [23, 26, 20, 18, 32]
# W = 67

# EX4:
# p = [414, 498, 545, 473, 543]
# w = [27, 29, 26, 30, 27]
# W = 67

# EX5:
p = [20, 10, 40, 15, 25]
w = [1, 3, 8, 7, 4]
W = 10


def swapList(sl,pos1,pos2):      
    sl[pos1], sl[pos2] = sl[pos2], sl[pos1]  
    return sl

def sort(p,w):
    for i in range(len(p)):
        for j in range(len(p)):
            if(p[i]/w[i] > p[j]/w[j]):
                swapList(p,i,j)
                swapList(w,i,j)



n = len(p)-1
numbest = 0
maxprofit = 0
bound = 0
totweight = 0


def knapsack ( i, profit, weight):
    global maxprofit
    if (weight <= W and profit > maxprofit):
        maxprofit = profit                                                                  
    if (promising(i,weight,profit)):
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
        knapsack (i + 1, profit, weight)
     
def promising (i,weight,profit):
    if (weight >= W):                           
        return False                       
    else:                                    
        j = i + 1                              
        bound = profit                        
        totweight = weight
        while (j <= n and totweight + w[j] <= W):
            totweight = totweight + w[j]         
            bound = bound + p[j]
            j = j+1
    k = j;                                  
    if (k <= n):                          
        bound = bound + (W - totweight)*p[k]/w[k]                                      
    return bound > maxprofit                           


start = default_timer()
sort(p,w)
knapsack(0, p[0], w[0])
print(maxprofit)                           
end = default_timer()
print(end-start)
  
