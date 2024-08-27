#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int firstDayBeenInAllRooms(vector<int> &nextVisit)
    {
        const int MOD = 1'000'000'007;
        int n = nextVisit.size();
        vector<long> s(n);
        for (int i = 0; i < n - 1; i++)
        {
            int j = nextVisit[i];
            s[i + 1] = (s[i] * 2 - s[j] + 2 + MOD) % MOD;
        }
        return s[n - 1];
    }
};

int main(int argc, char const *argv[])
{
    vector<int> nums;
    nums.push_back(5);
    for (int num: nums) {
        cout << num << " ";
    }
    nums.pop_back();
    cout << endl;
    nums.push_back(3);
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
