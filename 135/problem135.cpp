/* Problem
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
*/

/* Examples

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
*/
// time complexity O(n) really 3n
#include <iostream>

int candy(vector<int>& ratings) {
        
    // size of the input
    int n=ratings.size();
    
    // left pointer
    vector<int> left(n,1);

    // right pointer
    vector<int> right(n,1);

    // looping through all elements in ratings
    for(int i=1; i<n; i++){
        // if the next value is a higher rating give left one more candy
        if(ratings[i]>ratings[i-1]) left[i]=1+left[i-1];
    }

    // looping backwards through the array
    for(int i=n-2; i>=0; i--){
        // if the current value is greater than the last add to right
        if(ratings[i]>ratings[i+1]) right[i]=1+right[i+1];
    }

    long long ans=0;

    for(int i=0; i<n ; i++){
        ans+=(long long) max(left[i],right[i]);      
    }
    return ans;
}

int main() {
    std::cout << candy([1,0,2]) << std::endl;
    std::cout << candy([1,2,2]) << std::endl;
    return 0;
}