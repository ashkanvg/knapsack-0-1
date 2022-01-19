

p = [60, 100, 120]
w = [10, 20, 30]
W = 50
n = len(p)-1
numbest = 0
maxprofit = 0

weight = 0
profit = 0

def knapsack ( i, profit, weight):
    global maxprofit

    if (weight <= W and profit > maxprofit):
        maxprofit = profit                  
        #numbest = i;                         
        #bestset = include;                   
                                            
    if (promising(i)):
        #include [i + 1] = "yes"             
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
        #include [i + 1] = "no"              
        knapsack (i + 1, profit, weight)
     
   

def promising (i):
    global weight
    global profit
    #j, k
    #int totweight
    #  float bound;

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
                                             

    return bound > maxprofit;                           
   




knapsack(0, 0, 0)
print(maxprofit)                           
# for (j = 1; j <= numbest; j++)                // Show an optimal set of items.
#       cout << bestset[i]