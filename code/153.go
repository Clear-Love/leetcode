/*
 * @Author: lmio
 * @Date: 2023-02-20 20:27:22
 * @LastEditTime: 2023-02-20 20:47:47
 * @FilePath: /leetcode/code/153.go
 * @Description:153.寻找旋转排序数组中的最小值
 */
package code

func FindMin(nums []int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] > nums[right] {
			left = mid + 1
		}else {
			right = mid
		}
	}
	return nums[left]
}