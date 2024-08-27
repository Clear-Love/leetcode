#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        string s = countAndSay(n - 1);
        string res;
        int i = 0;
        while (i < s.size()) {
            int cnt = 1;
            while (i < s.size()-1 && s[i] == s[i+1]) {
                cnt++;
                i++;
            }
            res += format("{}{}", cnt, s[i]);
            i++;
        }
        return res;
    }
};