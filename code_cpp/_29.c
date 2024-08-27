/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-09 19:45:17
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 29. 两数相除
 */
#include <stdbool.h>
#include <limits.h>

int divide(int dividend, int divisor) {
    int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
    // 把负数转换为正数
    long did = dividend, div = divisor;
    did = (did > 0) ? did : -did;
    div = (div > 0) ? div : -div;
    long left = 0, right = 0xffffffff;
    long mid;
    while(left < right){
        // 防止溢出
        mid = left + (right-left+1) / 2; // 向上取整
        if(mid*div > did){ // 大了
            right = mid-1;
        }else{
            left = mid;
        }
    }
    left = left*sign;
    return left<INT_MIN ? INT_MIN : (left>INT_MAX ? INT_MAX : left);
}