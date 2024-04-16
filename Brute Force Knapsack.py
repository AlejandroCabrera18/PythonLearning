"""
Name: Alejandro Cabrera
Algorithm: Brute-force 0/1 Knapsack Problem
"""

def bfknapsack(W, weight, value, n):
    if n==0 or W ==0: #Base Case:
        #If capacity or length of value array is 0, return 0
        return 0
    if weight[n-1]>W:
        return bfknapsack(W, weight, value, n-1)
    else:
        return max(value[n-1] + bfknapsack(W-weight[n-1],weight, value, n-1),
                   bfknapsack(W,weight,value,n-1))
    #This function will run through each possible scenario
    #Resulting in time complexity of O(2^n)

value = [60,100,120] #value array
weight = [10,20,30] #Weight array
W = 50 #Capacity
n = len(value) #Size of value array 
print("Maximum value possible:",bfknapsack(W, weight, value, n))
