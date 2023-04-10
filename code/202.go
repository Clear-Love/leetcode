/*
 * @Author: lmio
 * @Date: 2023-04-10 10:10:45
 * @LastEditTime: 2023-04-10 10:37:17
 * @FilePath: /leetcode/code/202.go
 * @Description:202. 快乐数
 */
package code

func IsHappy(n int) bool {
	dict := map[int]bool{}
	var next func(int) bool
	next = func(v int) bool {
		if v == 1 {
			return true
		}
		if dict[v] {
			return false
		}
		dict[v] = true
		nextN := 0
		for v > 0 {
			num := v % 10
			nextN += num*num
			v /= 10
		}
		return next(nextN)
	}
	
	return next(n)
}