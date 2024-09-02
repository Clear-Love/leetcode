#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int countPairs(vector<int> &nums) {
        ranges::sort(nums);
        int ans = 0;
        unordered_map<int, int> cnt;
        for (int x : nums) {
            unordered_set<int> st = {x}; // 不交换
            string s = to_string(x);
            int m = s.size();
            for (int i = 0; i < m; i++) {
                for (int j = i + 1; j < m; j++) {
                    swap(s[i], s[j]);
                    st.insert(stoi(s)); // 交换一次
                    swap(s[i], s[j]);
                }
            }
            for (int v : st) {
                ans += cnt.contains(v) ? cnt[v] : 0;
            }
            cnt[x]++;
        }
        return ans;
    }
};