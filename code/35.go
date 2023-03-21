/*
 * @Author: lmio
 * @Date: 2023-02-03 02:15:32
 * @LastEditTime: 2023-02-19 23:26:43
 * @FilePath: /leetcode/code/35.go
 * @Description:35.搜索插入位置
 */

package code

func SearchInsert(nums []int, target int) int {
	left, right := 0, len(nums)-1
	if nums[right] < target{
		return right + 1
	}
	for left < right{
		mid := (left + right) >> 1
		if nums[mid] < target{
			left = mid + 1
		}else {
			right = mid
		}
	}
	return left
}