#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        auto maxCnt = [&](char ch) {
            int sum = 0;
            int ans = 0;
            for (int l = 0, r = 0; r < answerKey.size(); r++) {
                sum += answerKey[r] != ch;
                while (sum > k) {
                    sum -= answerKey[l++] != ch;
                }
                ans = max(ans, r - l + 1);
            }
            return ans;
        };
        return max(maxCnt('T'), maxCnt('F'));
    }
};