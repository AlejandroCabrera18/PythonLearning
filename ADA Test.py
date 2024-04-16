import sys

# Function to find the minimum number of coins required
# to get a total of `target` from set `coinSet`
def findMinCoins(coinSet, target):
 
    # `T[i]` stores the minimum number of coins needed to get a total of i
    T = [0] * (target + 1)
 
    for i in range(1, target + 1):
        # initialize the minimum number of coins needed to infinity
        T[i] = sys.maxsize
        # do for each coin
        for coin in range(len(coinSet)):
            # check if the index doesn't become negative by including
            # current coin `coin`
            if i - coinSet[coin] >= 0:
                result = T[i - coinSet[coin]]
                # if total can be reached by including current coin `coin`,
                # update the minimum number of coins needed `T[i]`
                if result != sys.maxsize:   
                    T[i] = min(T[i], result + 1)

    # `T[target]` stores the minimum number of coins needed to get a total of `target`
    return T[target]
 
 
if __name__ == '__main__':
    # coins of given denominations
    coinSet = [1, 3, 4]
    # total change required
    target = 6
    print("Target Value is: ", target)
    coins = findMinCoins(coinSet, target)
    if coins != sys.maxsize:
        print('The minimum number of coins required to get the desired change is',
            coins)

        
