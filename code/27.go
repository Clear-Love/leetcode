/*
 * @Author: lmio
 * @Date: 2023-04-09 15:13:48
 * @LastEditTime: 2023-04-09 15:35:35
 * @FilePath: /leetcode/code/27.go
 * @Description:27. 移除元素
 */
package code

func RemoveElement(nums []int, val int) int {
	for i := 0; i < len(nums); i++ {
		if nums[i] == val {
			j := i+1
			for j < len(nums) && nums[j] == val {
				j++
			}
			nums = append(nums[:i], nums[j:]...)
		}
	}
	return len(nums)
}