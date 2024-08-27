/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-06 14:30:08
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 141.环形链表
 */
#include<stdbool.h>
struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if (!head) {
        return false;
    }
    // 头到环长度为a，环长度为b slow走了x，则fast走了2x
    // 某时刻相遇，则a+nb == 2*(a+mb)
    struct ListNode* fast = head->next;
    struct ListNode* slow = head;
    while (fast && slow) {
        if (fast == slow) {
            return true;
        }
        slow = slow->next;
        fast = fast->next;
        if (fast) {
            fast = fast->next;
        }
    }
    return false;
}