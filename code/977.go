/*
 * @Author: lmio
 * @Date: 2023-02-03 03:49:19
 * @LastEditTime: 2023-02-19 23:36:18
 * @FilePath: /leetcode/code/977.go
 * @Description:977.有序数组的平方
 */
package code

func SortedSquares(nums []int) []int {
	//设置两个指针，分别指向数组的头和尾
	left, right := 0, len(nums)-1
	ptr := right
	for i := range nums{
		nums[i] *=nums[i]
	}
	
	result := make([]int, len(nums))
	for ptr != -1{
		if nums[left] > nums[right]{
			result[ptr] = nums[left]
			left++
		}else{
			result[ptr] = nums[right]
			right--
		}
		ptr--
	}
	return result
}