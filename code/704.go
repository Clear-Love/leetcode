/*
 * @Author: lmio
 * @Date: 2023-01-31 18:42:02
 * @LastEditTime: 2023-02-19 23:12:37
 * @FilePath: /leetcode/code/704.go
 * @Description:704:二分查找
 */

package code

func Search(nums []int, target int) int {
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] < target {
			left = mid +1
		}else {
			right = mid
		}
	}
	if target == nums[left]{
		return left
	}else{
		return -1
	}
}