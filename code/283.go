/*
 * @Author: lmio
 * @Date: 2023-02-03 04:51:52
 * @LastEditTime: 2023-02-19 23:28:47
 * @FilePath: /leetcode/code/283.go
 * @Description:283.移动零
 */
package code

func MoveZeroes(nums []int) {
	ptr := 0
	for key, val := range nums{
		if val == 0{
			continue
		}
		nums[key] = 0
		nums[ptr] = val
		ptr++
	}
}