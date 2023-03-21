/*
 * @Author: lmio
 * @Date: 2023-02-10 18:50:54
 * @LastEditTime: 2023-02-19 23:26:49
 * @FilePath: /leetcode/code/46.go
 * @Description:46.全排列
 */
package code

func Permute(nums []int) [][]int {
	ans := make([][]int, 0)
	path := make([]int, 0)
	isSel := make([]bool, len(nums))
	n := len(nums)
	var backtrace func(int)
	backtrace = func(length int) {
		if length == n {
			ans = append(ans, append([]int{}, path...))
			return
		}
		for i := 0; i < n; i++ {
			if isSel[i] {
				continue
			}
			isSel[i] = true
			path = append(path, nums[i])
			backtrace(length+1)
			isSel[i] = false
			path = path[:len(path)-1]
		}
	}
	return ans
}