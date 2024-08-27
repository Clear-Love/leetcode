/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-04-01 03:47:23
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 建造房屋
 */
#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    function<int(int, int)> dfs = [&](int i, int c) ->int {
        if (i == n) return min(c, m);
        int res = 0;
        for (int j = 1; j < min(m+1, c); j++) {
            res += dfs(i+1, c-j);
        }
        return res;
    };
    cout << dfs(1, k) << endl;
    return 0;
}
