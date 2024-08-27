/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-31 21:06:58
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2409. 统计共同度过的日子数
 */
#include<bits/stdc++.h>
using namespace std;
int DAYS[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int calc_day(string t) {
    int month = (t[0] - '0')*10 + t[1]-'0';
    int day = (t[3] - '0')*10 + t[4]-'0';
    for (int i = 0; i < month-1; i++) {
        day += DAYS[i];
    }
    return day;
};

class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int left = calc_day(max(arriveAlice, arriveBob));
        int right = calc_day(min(leaveAlice, leaveBob));
        return max(right-left+1, 0);
    }
};