#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        vector<string> v;
        int i = 1;
        while (i < path.size()) {
            string s;
            while (i < path.size() && path[i] != '/') {
                s += path[i];
                i++;
            }
            while (path[i] == '/') {
                i++;
            }

            if (s == "..") {
                if (!v.empty()) {
                    v.pop_back();
                }
            } else if (!s.empty() && s != ".") {
                v.push_back(s);
            }
        }
        string res;
        for (auto &s : v) {
            res += "/" + s;
        }
        return res.empty() ? "/" : res;
    }
};