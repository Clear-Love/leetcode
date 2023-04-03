/*
 * @Author: lmio
 * @Date: 2023-04-02 15:30:36
 * @LastEditTime: 2023-04-02 15:42:47
 * @FilePath: /leetcode/code/213.go
 * @Description:213. 打家劫舍 II
 */
package code

import "leetcode/template"

func RobII(nums []int) int {
	// 返回不偷窃第一家与不偷窃最后一家的最大值
	return template.Max(RobI(nums[1:]), RobI(nums[:len(nums)-1]))
}