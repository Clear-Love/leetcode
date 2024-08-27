/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-08-22 15:39:45
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 92. 反转链表 II
 */
#include "utils.h"
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int left, int right) {
        auto dummy = new ListNode(-1, head);
        auto pre = dummy;
        auto cur = head;
        for (int i = 0; i < left - 1; ++i) {
            pre = pre->next;
        }
        cur = pre->next;
        auto last = cur;
        for (int i = 0; i < right - left; ++i) {
            auto tmp = cur->next;
            cur->next = tmp->next;
            tmp->next = pre->next;
            pre->next = tmp;
        }
        return dummy->next;
    }
};