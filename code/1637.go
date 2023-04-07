/*
 * @Author: lmio
 * @Date: 2023-03-30 10:28:03
 * @LastEditTime: 2023-04-07 14:35:17
 * @FilePath: /leetcode/code/1637.go
 * @Description:1637. 两点之间不包含任何点的最宽垂直区域
 */
package code

import (
	"leetcode/utils"
	"sort"
)

func MaxWidthOfVerticalArea(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] - points[j][0] < 0
	})
	max := points[1][0] - points[0][0]
	for i := 2; i < len(points); i++ {
		max = utils.Max(max, points[i][0] - points[i-1][0])
	}
	return max
}