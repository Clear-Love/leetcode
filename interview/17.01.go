/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2023-08-18 17:39:21
 * @LastEditors: lmio 2091319361@qq.com
 * @Description:面试题 17.01. 不用加号的加法
 */
package interview

func Add(a, b int) int {
    for b != 0 {
        carry := uint(a&b) << 1
        a ^= b
        b = int(carry)
    }
    return a
}