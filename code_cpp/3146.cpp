#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findPermutationDifference(string s, string t) {
        auto m = unordered_map<int, int>();
        for (int i = 0; i < s.size(); i++) {
            m[s[i]] = i;
        }
        int res = 0;
        for (int i = 0; i < t.size(); i++) {
            res += abs(i-(m[t[i]]));
        }
        return res;
    }
};