/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-05 16:01:45
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2643. 一最多的行
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        int n = mat.size();
        vector<int> res(2, 0);
        for (int i = 0; i < n; i++) {
            int s = 0;
            for (auto num: mat[i]) {
                s += num;
            }
            if (s > res[1]) {
                res[0] = i;
                res[1] = s;
            }
        }
        return res;
    }
};