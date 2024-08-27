/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-07 21:14:10
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: LCR 123. 图书整理 I
 */
#include<stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};

int N = 0;
int* reverseBookList(struct ListNode* head, int* returnSize) {
    if (head == NULL) {
        *returnSize = 0;
        return malloc(sizeof(int)*N);
    }
    N++;
    int* res = reverseBookList(head->next, returnSize);
    res[(*returnSize)++] = head->val;
    return res;
}