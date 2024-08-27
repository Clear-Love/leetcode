/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-09 19:08:12
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 29. 两数相除
 */
#include <limits.h>
int divide(int dividend, int divisor) {
    long div=divisor, did=dividend;
    int sign = 1;
    if((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)){
        sign = -1;
    }
    long res = 0;
    did = did > 0 ? did : -did;
    div = div > 0 ? div : -div;
    for (int i = 31; i >= 0; i--) {
        if (did >= (div << i)) {
            res += (long)1 << i;
            did -= (div << i);
        }
    }
    res = sign * res;
    return res<INT_MIN? INT_MIN: res>INT_MAX ? INT_MAX : res;
}