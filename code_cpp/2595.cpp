#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> evenOddBit(int n) {
        const static int MASK = 0x5555;
        return {__builtin_popcount(n & MASK),
                __builtin_popcount(n & (MASK >> 1))};
    }
};