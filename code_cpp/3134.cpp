#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int medianOfUniquenessArray(vector<int> &nums) {
        int left = 0, right = nums.size();
        size_t n = nums.size();
        uint64_t k = (n * (n + 1) / 2 + 1) / 2; // 向上取整
        auto check = [&](int mid) {
            unordered_map<int, int> freq;
            int left = 0, right = 0;
            uint64_t cnt = 0;
            while (right < nums.size()) {
                freq[nums[right]]++;
                // 元素个数要小于mid
                while (freq.size() > mid) {
                    auto it = freq.find(nums[left]);
                    it->second--;
                    if (it->second == 0) {
                        freq.erase(it);
                    }
                    left++;
                }
                cnt += right - left + 1;
                if (cnt >= k)
                    return true;
                right++;
            }
            return false;
        };
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};