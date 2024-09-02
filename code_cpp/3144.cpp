#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int minimumSubstringsInPartition(string s) {
        int n = s.size();
        vector<int> d(n + 1, INT_MAX);
        unordered_map<char, int> cnts;
        d[0] = 0;
        for (int i = 1; i <= n; i++) {
            int max_cnt = 0;
            cnts.clear();
            for (int j = i; j >= 1; j--) {
                cnts[s[j - 1]]++;
                max_cnt = max(max_cnt, cnts[s[j - 1]]);
                if (max_cnt * cnts.size() == (i - j + 1) && d[j - 1] != INT_MAX) {
                    d[i] = min(d[i], d[j - 1] + 1);
                }
            }
        }
        return d[n];
    }
};