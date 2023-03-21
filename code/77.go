/*
 * @Author: lmio
 * @Date: 2023-02-10 17:24:56
 * @LastEditTime: 2023-02-22 09:52:30
 * @FilePath: /leetcode/code/77.go
 * @Description:77.组合
 */
package code

func Combine(n int, k int) [][]int {
	ans := make([][]int, 0)
	path := make([]int, 0)
	var backtrack func(int)
	backtrack = func(selval int) {
		if len(path) == k {
			ans = append(ans, append([]int{}, path...))
			return
		}
		for i := selval+1; i <= n; i++ {
			path = append(path, i)
			backtrack(i)
			path = path[:len(path)-1]
		}
	}
	backtrack(0)
	return ans
}