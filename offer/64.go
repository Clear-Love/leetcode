/*
 * @Author: lmio
 * @Date: 2023-04-09 12:48:55
 * @LastEditTime: 2023-04-09 12:54:37
 * @FilePath: /leetcode/offer/64.go
 * @Description:剑指 Offer 64. 求1+2+…+n
 */
package offer

func SumNums(n int) int {
	res := 0
    var sum func(int) bool
    sum = func(n int) bool {
        res += n
        return n > 0 && sum(n-1)
    }
    sum(n)
    return res
}