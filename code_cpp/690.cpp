#include <bits/stdc++.h>

using namespace std;

class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};

class Solution {
public:
    int getImportance(vector<Employee *> employees, int id) {
        unordered_map<int, pair<int, vector<int>>> mp;
        for (auto e : employees) {
            mp[e->id] = {e->importance, e->subordinates};
        }
        auto dfs = [&](auto &&dfs, int id) ->int {
            auto [importance, subordinates] = mp[id];
            for (auto sub : subordinates) {
                importance += dfs(dfs, sub);
            }
            return importance;
        };
        return dfs(dfs, id);
    }
};