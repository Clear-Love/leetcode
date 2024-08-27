/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-08 17:21:52
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 1652. 拆炸弹
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdlib.h>
#include<stdio.h>

int* decrypt(int* code, int codeSize, int k, int* returnSize) {
    int* res = (int*)calloc(codeSize, sizeof(int));
    int start, end;
    if (k > 0) {
        end = k+1, start = 1;
    }else {
        end = 0, start = k;
    }
    for (int i = start; i < end; i++) {
        for (int j = 0; j < codeSize; j++) {
            res[j] += code[(j+i+codeSize)%codeSize];
        }
    }
    *returnSize = codeSize;
    return res;
}