/*
 * @Author: lmio
 * @Date: 2023-04-03 19:00:42
 * @LastEditTime: 2023-04-07 14:36:22
 * @FilePath: /leetcode/code/62.go
 * @Description:62. 不同路径
 */
package code

import (
	"leetcode/utils"
)

func UniquePaths(m, n int) int {
	num, sum := int64(m-1), int64(n+m-2)
	res := int(utils.CombinationsCount(sum, num).Int64())
	return res
}