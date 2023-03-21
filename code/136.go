/*
 * @Author: lmio
 * @Date: 2023-02-13 21:50:20
 * @LastEditTime: 2023-02-19 23:27:38
 * @FilePath: /leetcode/code/136.go
 * @Description:136.只出现一次的数字
 */
package code

func SingleNumber(nums []int) (res int) {
	for _, val := range nums {
		res ^= val
	}
	return res
}