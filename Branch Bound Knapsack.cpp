// C++ program to solve knapsack problem using
// branch and bound
//By: Alejandro Cabrera
#include <bits/stdc++.h>
using namespace std;

struct Item
{
    float weight; //Stores an item's weight
    int value;    //Stores an item's value
};

// Node structure to store information of decision
// tree
struct Node
{
    int level, profit, bound; // Level is a node's level in the tree,
    //Profit is the total profit of nodes from the root to the current node
    //Bound is the upper bound of max profit in the subtree of this current node
    float weight; // Weight to store the sum of weight stored up to this current node
};

bool compare(Item a, Item b)
{
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2; //This function is useful to sort the array of items in terms of value/weight
}

int bound(Node u, int n, int W, Item arr[])
{
    if (u.weight >= W) //If a node's weight is above the capacity, the bound should be 0
        return 0;
    int profit_bound = u.profit; // initialize bound on profit by the current profit
    int j = u.level + 1;         //Necessary to include items from a level ahead of the current item index
    int totalweight = u.weight;
    while ((j < n) && (totalweight + arr[j].weight <= W)) //Checks index and knapsack capacity
    {
        profit_bound += arr[j].value;
        totalweight += arr[j].weight;
        j++;
    }

    // If k is not n, include last item partially for
    // upper bound on profit
    if (j < n)
        profit_bound += (W - totalweight) * arr[j].value /
                        arr[j].weight;

    return profit_bound;
    // Returns bound of profit in subtree rooted within current node,u.
    // Uses greedy approach to find max bound
}

int bbknapsack(int W, Item arr[], int n)
{
    sort(arr, arr + n, compare); //Sorts items by value/weight order
    queue<Node> Q;               // make a queue
    Node u, v;                   // Create nodes u and v

    // prototype node to start
    u.level = -1;
    u.profit = u.weight = 0;
    Q.push(u);
    // Repeatedly select an item from the decision tree and compute
    // the profit of all the children of the selected item and save to maxProfit
    int maxProfit = 0;
    while (!Q.empty())
    {
        // Dequeue a node
        u = Q.front();
        Q.pop();

        // If starting node, give it level 0
        if (u.level == -1)
            v.level = 0;

        // If next level has nothing
        if (u.level == n - 1)
            continue;

        v.level = u.level + 1; //If not the last node, increment the level and compute
        // the profit of the child nodes

        // Takes current level's item and adds current
        // level's weight and value to node u's
        // weight and value
        v.weight = u.weight + arr[v.level].weight;
        v.profit = u.profit + arr[v.level].value;

        // If cumulated weight is less than capacity and
        // profit is greater than the previous profit,
        // update maxprofit
        if (v.weight <= W && v.profit > maxProfit)
            maxProfit = v.profit;

        // Get the upper bound on profit to decide
        // whether to add v to Q or not.
        v.bound = bound(v, n, W, arr);

        // If bound value is greater than profit,
        // then only push into queue for further
        // consideration
        if (v.bound > maxProfit)
            Q.push(v);

        // Repeat, but without taking
        // the item in knapsack
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, n, W, arr);
        if (v.bound > maxProfit)
            Q.push(v);
    }

    return maxProfit; // Returns the max profit we can achieve with the given capacity, W
}

int main() //Main Function
{
    int W = 20;                                                  // capacity of knapsack
    Item arr[] = {{7, 90}, {4, 50}, {8, 100}, {5, 95}, {2, 30}}; //Items available to be stored
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Maximum possible profit = "
         << bbknapsack(W, arr, n);

    return 0;
}
