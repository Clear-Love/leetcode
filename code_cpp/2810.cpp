/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-01 15:49:54
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2810. 故障键盘
 */
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string finalString(string s) {
        deque<char> q;
        bool tail = true;
        for (char c : s) {
            if (c == 'i') tail = !tail; // 修改添加方向
            else if (tail) q.push_back(c); // 加尾部
            else q.push_front(c); // 加头部
        }
        return tail ? string(q.begin(), q.end()) : string(q.rbegin(), q.rend());
    }
};