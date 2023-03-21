/*
 * @Author: lmio
 * @Date: 2023-02-12 21:07:46
 * @LastEditTime: 2023-02-19 23:35:52
 * @FilePath: /leetcode/code/724.go
 * @Description:724.寻找中心数组的中心下标
 */
package code

func PivotIndex(nums []int) int {
	total := 0
	for _, val := range nums {
		total += val
	}
	sum := 0
	for i, v := range nums {
		if total - sum -v == sum {
			return i
		}
		sum += v
	}
	return -1
}