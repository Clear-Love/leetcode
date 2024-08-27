#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        int cnts[26] = {0};
        for (auto c : s) {
            cnts[c - 'a']++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (cnts[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
};