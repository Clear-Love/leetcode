/*
 * @Author: lmio
 * @Date: 2023-02-20 20:48:39
 * @LastEditTime: 2023-02-20 21:40:05
 * @FilePath: /leetcode/code/162.go
 * @Description:162.寻找峰值
 */
package code

func FindPeakElement(nums []int) int {
	length := len(nums)
	if length == 1 || nums[0] > nums[1] {
		return 0
	}
	left, right := 0, length-1
	if nums[right] > nums[right-1] {
		return right
	}
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] < nums[left] {
			right = mid - 1
		}else if nums[mid] <= nums[right] {
			left = mid + 1
		}else {
			right--
		}
	}
	return left
}