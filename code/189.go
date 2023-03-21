/*
 * @Author: lmio
 * @Date: 2023-02-03 04:22:08
 * @LastEditTime: 2023-02-19 23:27:49
 * @FilePath: /leetcode/code/189.go
 * @Description:189.轮转数组
 */
package code

func Rotate(nums []int, k int) {
	length := len(nums)
	k %= length
	copied := make([]int, length)
	copy(copied, nums)

	ptr := 0
	for i := length - k; i < length; i++ {
		nums[ptr] = copied[i]
		ptr++
	}
	for i := 0; ptr < length; i++ {
		nums[ptr] = copied[i]
		ptr++
	}
}
