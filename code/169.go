/*
 * @Author: lmio
 * @Date: 2023-04-16 17:46:56
 * @LastEditTime: 2023-04-16 18:50:49
 * @FilePath: /leetcode/code/169.go
 * @Description:169. 多数元素
 */
package code

func MajorityElement(nums []int) int {
	candidate := 0
	count := 0
	for _, num :=range nums {
		if count == 0 {
			candidate = num
		}
		if num == candidate {
			count++
		}else {
			count--
		}
	}
	return candidate
}