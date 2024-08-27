/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-31 21:33:45
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2410. 运动员和训练师的最大匹配数
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());
        int idx = 0;
        int n = trainers.size();
        int res = 0;
        for (int i = 0; i < players.size(); i++) {
            int p = players[i];
            while (idx < n && trainers[idx] < p) {
                idx++;
            }
            if (idx >= n) break;
            idx++;
            res++;
        }
        return res;
    }
};