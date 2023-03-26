/*
 * @Author: lmio
 * @Date: 2023-03-26 23:52:14
 * @LastEditTime: 2023-03-26 23:57:15
 * @FilePath: /leetcode/offer/53-II.go
 * @Description:剑指 Offer 53 - II. 0～n-1中缺失的数字
 */
package offer

func MissingNumber(nums []int) int {
	left, right := 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] == mid {
			left = mid + 1
		}else {
			right = mid - 1
		}
	}
	return left
}