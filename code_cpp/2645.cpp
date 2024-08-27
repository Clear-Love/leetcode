/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-05 16:33:15
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2645. 构造有效字符串的最少插入数
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int addMinimum(string word) {
        int t = 1, n = word.size();
        for (int i = 1; i < n; i++) {
            if (word[i] <= word[i-1]) {
                t += 1;
            }
        }
        return t*3 - word.size();
    }
};