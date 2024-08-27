#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maximumScore(vector<int>& cards, int cnt) {
        sort(cards.begin(), cards.end(), greater<int>());
        uint64_t s = 0;
        int minj = INT_MAX, mino = INT_MAX;
        for (int i = 0; i < cnt; i++) {
            s += cards[i];
            if (cards[i]%2 == 0) {
                mino = min(mino, cards[i]);
            } else {
                minj = min(minj, cards[i]);
            }
        }
        if (s%2 != 0) {
            if (mino == INT_MAX) {
                // 全是奇数，取一个最大的偶数替换
                for (int i = cnt; i < cards.size(); i++) {
                    if (cards[i]%2 == 0) {
                        s += cards[i] - minj;
                        return s;
                    }
                }
                // 全是奇数，没有偶数
                return 0;
            }
            if (cnt == cards.size()) {
                // 全部取完
                return 0;
            }
            bool fo = false, fj = false;
            int chan = INT_MIN;
            for (int i = cnt; i < cards.size(); i++) {
                if (!fj && cards[i]%2 != 0) {
                    // 取出偶数换为奇数
                    chan = max(chan, cards[i] - mino);
                    fj = true;
                } else if (!fo && cards[i]%2 == 0){
                    // 取出奇数换为偶数
                    chan = max(chan, cards[i] - minj);
                    fo = true;
                }
                if (fo && fj) {
                    break;
                }
            }
            s += chan;
        }
        return s;
    }
};