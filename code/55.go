/*
 * @Author: lmio
 * @Date: 2023-02-12 23:50:43
 * @LastEditTime: 2023-02-19 23:26:55
 * @FilePath: /leetcode/code/55.go
 * @Description:55.跳跃游戏
 */
package code

func CanJump(nums []int) bool {
	prevNode := len(nums) - 1
	for i := prevNode-1; i >= 0; i-- {
		if nums[i] >= prevNode - i {
			prevNode = i
		}
	}
	return nums[0] >= prevNode
}