/*
 * @Author: lmio
 * @Date: 2023-02-11 17:28:14
 * @LastEditTime: 2023-02-19 23:27:01
 * @FilePath: /leetcode/code/70.go
 * @Description:70.爬楼梯
 */
package code

func ClimbStairs(n int) int {
	p, q, r := 0, 0, 1
	for i := 1; i <= n; i++ {
		p = q
		q = r
		r = p + q
	}
	return r
}
