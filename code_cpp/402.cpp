#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        deque<char> stack;
        for (int i = 0; i < num.size(); i++) {
            while (k && !stack.empty() && stack.back() > num[i]) {
                stack.pop_back();
                k--;
            }
            stack.push_back(num[i]);
        }
        while (k--) {
            stack.pop_back();
        }
        while(!stack.empty() && stack.front() == '0') {
            stack.pop_front();
        }
        auto str = string(stack.begin(), stack.end());
        return str == ""? "0" : str;
    }
};