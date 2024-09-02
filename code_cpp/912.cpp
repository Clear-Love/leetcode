#include <bits/stdc++.h>

using namespace std;

class Solution {
    template <typename T, typename _Compare = less<T>>
    void heapify(vector<T> &nums, _Compare cmp = _Compare()) {
        // 从非叶子节点开始，从后往前
        for (int i = nums.size() / 2 - 1; i >= 0; i--) {
            _heapify(nums, i, nums.size(), cmp);
        }
    }

    template <typename T, typename _Compare = less<T>>
    void _heapify(vector<T> &nums, int i, int n, _Compare cmp = _Compare()) {
        auto j = 2 * i + 1;
        while (j < n) {
            if (j + 1 < n && cmp(nums[j + 1], nums[j])) {
                j++;
            }
            if (cmp(nums[i], nums[j])) {
                break;
            } else {
                swap(nums[i], nums[j]);
                i = j;
                j = 2 * i + 1;
            }
        }
    }

public:
    vector<int> sortArray(vector<int> &nums) {
        heapify(nums, greater<int>());
        for (int i = nums.size() - 1; i >= 1; i--) {
            swap(nums[0], nums[i]);
            _heapify(nums, 0, i, greater<int>());
        }
        return nums;
    }
};