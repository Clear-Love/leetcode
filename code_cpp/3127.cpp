#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canMakeSquare(vector<vector<char>>& grid) {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                int cnts[2] = {0};
                for (int x = i; x < i + 2; x++) {
                    for (int y = j; y < j + 2; y++) {
                        if (grid[x][y] == 'W') {
                            cnts[0]++;
                        } else {
                            cnts[1]++;
                        }
                    }
                }
                if (cnts[0] >= 3 || cnts[1] >= 3) {
                    return true;
                }
            }
        }
        return false;
    }
};