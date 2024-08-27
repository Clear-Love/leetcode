/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-03-31 17:13:34
 * @LastEditors: lmio 2091319361@qq.com
 * @Description:
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  	vector<string> split(string& preorder) {
		stringstream ss(preorder);
		string temp;
		vector<string> v;
		while (getline(ss, temp, ',')) v.push_back(temp);
		return v;
  	}
  	bool isValidSerialization(string preorder) {
		vector<string> ss = split(preorder);
		int n = ss.size();
		int diff = 1;
		for (int i = 0, m = 0; i < n; i++) {
			diff -= 1;
			if (ss[i] != "#") diff += 2;
			if (diff < 0) {
				return false;
			}
		}
		return diff == 0;
	}
};