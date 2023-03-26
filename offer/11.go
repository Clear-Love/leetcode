/*
 * @Author: lmio
 * @Date: 2023-03-26 21:24:37
 * @LastEditTime: 2023-03-26 22:34:07
 * @FilePath: /leetcode/offer/11.go
 * @Description:剑指 Offer 11. 旋转数组的最小数字
 */
package offer

func MinArray(numbers []int) int {
	left, right := 0, len(numbers)-1
	for left < right {
		mid := (left + right) >> 1
		if numbers[mid] > numbers[right] {
			left = mid + 1
		}else if numbers[mid] < numbers[right]{
			right = mid
		}else {
			right--
		}
	}
	return numbers[left]
}