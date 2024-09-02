#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int xorOperation(int n, int start) {
        auto sumXor = [](int x) -> int {
            if (x % 4 == 0) {
                return x;
            }
            if (x % 4 == 1) {
                return 1;
            }
            if (x % 4 == 2) {
                return x + 1;
            }
            return 0;
        };
        int s = start >> 1, e = n & start & 1;
        int ret = sumXor(s - 1) ^ sumXor(s + n - 1);
        return ret << 1 | e;
    }
};