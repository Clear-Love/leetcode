/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-08-23 14:52:40
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 11. 盛最多水的容器
 */
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        auto n = height.size();
        int l = 0, r = n - 1;
        int res = 0;
        while(l < r){
            res = max(res, min(height[l], height[r]) * (r - l));
            if(height[l] < height[r]){
                l++;
            } else{
                r--;
            }
        }
        return res;
    }
};