/*
 * @Author: lmio
 * @Date: 2023-03-29 10:07:29
 * @LastEditTime: 2023-03-29 10:11:29
 * @FilePath: /leetcode/offer/10-II.go
 * @Description:剑指 Offer 10- II. 青蛙跳台阶问题
 */
package offer

func NumWays(n int) int {
	var mod int = 1e9 + 7
	prev2, prev1, res := 1, 1, 0
    if n == 0 {
        return 1
    }
	if n < 2 {
		return n
	}
	for i := 2; i <= n; i++ {
		res = (prev1 + prev2) % mod
		prev2 = prev1
		prev1 = res
	}
	return res	
}