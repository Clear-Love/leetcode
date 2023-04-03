/*
 * @Author: lmio
 * @Date: 2023-04-03 09:53:35
 * @LastEditTime: 2023-04-03 09:57:40
 * @FilePath: /leetcode/offer/57.go
 * @Description:剑指 Offer 57. 和为s的两个数字
 */
package offer

func TwoSum(nums []int, target int) [] int {
	left, right := 0, len(nums)-1
	for left < right {
		sum := nums[left] + nums[right] 
		if sum == target {
			return []int{nums[left], nums[right]}
		}else if sum > target {
			right--
		}else {
			left++
		}
	}
	return nil
}