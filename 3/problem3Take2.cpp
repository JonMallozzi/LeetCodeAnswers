#include <iostream>
#include <string>
#include <unordered_map>

int lengthOfLongestSubstring(std::string s) {

  if(s.empty())
            return 0;
        std::unordered_map<char,int> m;
        int ans=1,left=-1;
        for(int i=0;i<s.size();++i){
            if(m.find(s[i])!=m.end() && m[s[i]]>=left){
                left=m[s[i]];
            }
            ans=std::max(ans,i-left);
            m[s[i]]=i;
        }
        return ans; 
        
}

int main(){
    std::cout << lengthOfLongestSubstring("pwwkew") << std::endl;
    return 0;
}