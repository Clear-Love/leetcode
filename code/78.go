/*
 * @Author: lmio
 * @Date: 2023-03-30 09:22:11
 * @LastEditTime: 2023-03-30 09:56:22
 * @FilePath: /leetcode/code/78.go
 * @Description:78.子集
 */
package code

func Subsets(nums []int) [][]int {
	res := [][]int{}
	ans := []int{}
	var backbrack func(l, k int)
	backbrack = func (l, k int)  {
		if len(ans) == l {
			res = append(res, append([]int{}, ans...))
			return
		}
		for i := k; i < len(nums); i++ {
			ans = append(ans, nums[i])
			backbrack(l, i+1)
			ans = ans[:len(ans)-1]
		}
	}
	for i := 0; i <= len(nums); i++ {
		backbrack(i, 0)
	}
	return res
}