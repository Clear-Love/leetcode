#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int> &nums, int k) {
        priority_queue<int> maxHeap; // 大根堆, 存储较小的一半元素
        priority_queue<int, vector<int>, greater<int>>
            minHeap; // 小根堆, 存储较大的一半元素
        for (int i = 0; i < k; i++) {
            maxHeap.push(nums[i]);
        }
        for (int i = 0; i < k / 2; i++) {
            // k 为奇数时， maxHeap 比 minHeap 多一个元素
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        }
        auto res = vector<double>();
        if (k % 2 == 0) {
            res.push_back(((int64_t)maxHeap.top() + minHeap.top()) / 2.0);
        } else {
            res.push_back(maxHeap.top() * 1.0);
        }

        unordered_map<int, int> deled;
        for (int i = k; i < nums.size(); i++) {
            int balance = 0;
            // 删除滑动窗口最左边的元素
            deled[nums[i - k]]++;
            if (!maxHeap.empty() && nums[i - k] <= maxHeap.top()) {
                balance--;
            } else {
                balance++;
            }
            // 插入滑动窗口最右边的元素
            if (!maxHeap.empty() && nums[i] < maxHeap.top()) {
                maxHeap.push(nums[i]);
                balance++;
            } else {
                minHeap.push(nums[i]);
                balance--;
            }
            if (balance > 0) {
                minHeap.push(maxHeap.top());
                maxHeap.pop();
                balance--;
            }
            if (balance < 0) {
                maxHeap.push(minHeap.top());
                minHeap.pop();
                balance++;
            }
            while (!maxHeap.empty() && deled[maxHeap.top()] > 0) {
                deled[maxHeap.top()]--;
                maxHeap.pop();
            }
            while (!minHeap.empty() && deled[minHeap.top()] > 0) {
                deled[minHeap.top()]--;
                minHeap.pop();
            }

            if (k % 2 == 0) {
                res.push_back(((int64_t)maxHeap.top() + minHeap.top()) / 2.0);
            } else {
                res.push_back(maxHeap.top() * 1.0);
            }
        }
        return res;
    }
};