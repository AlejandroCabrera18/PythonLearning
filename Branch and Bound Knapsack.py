"""
Name: Alejandro Cabrera
Algorithm: Branch and Bound 0/1 Knapsack Problem
"""
class Item:
    def __init__(self,w,v):
        self.weight = w
        self.value =v

class Node:
    def __init(self,lvl,profit,bound,w):
        self.level = lvl
        self.profit = profit
        self.bound = bound
        self.weight = w

def compare(a,b):
    r1 = a.value/a.weight
    r2 = b.value/b.weight
    return r1>r2;

def bound(node,n,W,itemArray):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totalWeight = node.weight

    while((j<n) and (totalWeight+itemArray[j].weight <= W)):
        totalweight = totalWeight + itemArray[j].weight
        profit_bound = profit_bound + itemArray[j].value
        j++
    if j<n:
        profit_bound = profit_bound + ((W-totalWeight)*(itemArray[j].value/itemArray[j].weight))
    return profit_bound    

def bbknapsack(W, itemArray, n):
    sort()
    Q = []
    u = Node(-1,0,0)
    Q.append(u)
    
value = [60,100,120] #value array
weight = [10,20,30] #Weight array
W = 50 #Capacity
n = len(value) #Size of value array 
print("Maximum value possible:",bfknapsack(W, weight, value, n))
