#include <iostream>
#include <string>
#include <unordered_set>

int lengthOfLongestSubstring(std::string s) {

    //checks for the space substring
    if(s == " "){
        return 1;
    }

    std::unordered_set <char> subString ;
    int currentMaxLength = 0;

    for(char letter : s){

         if(s.empty())
            return 0;
        
        //checks if the hashSet contains the current letter
        if(subString.find(letter) != subString.end()){

            //updates the maxLength only if the current subString is longer
            if(subString.size() > currentMaxLength){
                currentMaxLength = subString.size();
            }

            //removes the dupe from the front of the hashSet
            subString.erase(letter);
        }

        //checks if its possible to have longer substring
        if(currentMaxLength > s.length() - currentMaxLength){
            return currentMaxLength;
       }

        subString.insert(letter);
    }

    //updates the result if it never has a dupe
    if (subString.size() > currentMaxLength){
        currentMaxLength = subString.size();
    }

    for(char letter: subString){
        std::cout << letter << std::endl;
    }

    return currentMaxLength;
        
}

int main(){
    std::cout << lengthOfLongestSubstring("pwwkew") << std::endl;
    return 0;
}