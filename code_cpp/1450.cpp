#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int busyStudent(vector<int> &startTime, vector<int> &endTime,
                    int queryTime) {
        int n = startTime.size();
        vector<int> cnt(1002, 0);
        for (int i = 0; i < n; i++) {
            cnt[startTime[i]]++;
            cnt[endTime[i] + 1]--;
        }
        int ans = 0;
        for (int i = 0; i <= queryTime; i++) {
            ans += cnt[i];
        }   
        return ans;
    }
};