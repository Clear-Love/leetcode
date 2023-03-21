/*
 * @Author: lmio
 * @Date: 2023-02-03 05:05:35
 * @LastEditTime: 2023-02-19 23:11:16
 * @FilePath: /leetcode/code/167.go
 * @Description:167.两数之和 II - 输入有序数组
 */
package code

func TwoSum(numbers []int, target int) []int {
	left := 0
	right := len(numbers)
	for left < right {
		l := numbers[left]
		r := numbers[right]
		if l+r == target {
			return []int{left + 1, right + 1}
		} else if l+r < target {
			left++
		} else {
			right--
		}
	}
	return nil
}