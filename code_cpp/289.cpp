#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>> &board) {
        auto d = vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0},  {-1, 0},
                                        {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        int n = board.size(), m = board[0].size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int cnt = 0;
                for (auto &[dx, dy] : d) {
                    int x = i + dx, y = j + dy;
                    if (x < 0 || x >= n || y < 0 || y >= m) {
                        continue;
                    }
                    cnt += (board[x][y] & 1); // 只统计低位，即当前状态
                }
                if (board[i][j] == 0 && cnt == 3) {
                    // 如果死细胞周围正好有三个活细胞，则该位置死细胞复活
                    board[i][j] ^= 2;
                } else if (board[i][j] == 1 && (cnt == 2 || cnt == 3)) {
                    // 如果活细胞周围正好有两个或三个活细胞，则该位置活细胞仍然存活
                    board[i][j] ^= 2;
                }
            }
        }
        for (auto &row : board) {
            for (auto &cell : row) {
                cell >>= 1;
            }
        }
    }
};