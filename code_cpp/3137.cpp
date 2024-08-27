#include <bits/stdc++.h>
#include <string_view>

using namespace std;

class Solution {
public:
    int minimumOperationsToMakeKPeriodic(string word, int k) {
        unordered_map<string_view, int> cnts;
        for (int i = 0; i < word.size(); i+=k) {
            cnts[{word.c_str()+i, word.c_str()+i+k}] += 1;
        }
        return word.size()/k - max(cnts.begin(), cnts.end(), [](auto& a, auto& b) {
            return a->second < b->second;
        })->second;
    }
};