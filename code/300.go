/*
 * @Author: lmio
 * @Date: 2023-04-06 09:35:31
 * @LastEditTime: 2023-04-06 10:20:41
 * @FilePath: /leetcode/code/300.go
 * @Description:300. 最长递增子序列
 */
package code

func LengthOfLIS(nums []int) int {
	tails := make([]int, len(nums))
	res := 0
	for _, num := range nums {
		i, j := 0, res
		// 找到小于num的第一个值
		for i < j {
			mid := (i + j) / 2
			if num > tails[mid] {
				i = mid + 1
			}else {
				j = mid
			} 
		}
		tails[i] = num
		if res == i {
			res++
		}
	}
	return res;
}