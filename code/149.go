/*
 * @Author: lmio
 * @Date: 2023-04-10 10:44:31
 * @LastEditTime: 2023-04-10 22:51:47
 * @FilePath: /leetcode/code/149.go
 * @Description:149. 直线上最多的点数
 */
package code

import (
	"leetcode/utils"
	"strconv"
)

func MaxPoints(points [][]int) int {
	max := 0
	for i := 0; i < len(points); i++ {
		// 经过points[i]的直线点的个数
		m := map[string]int{}
		x1, y1 := points[i][0], points[i][1]
		for j := i+1; j < len(points); j++ {
			dx, dy := points[j][0]-x1, points[j][1]-y1
			g := utils.Gcd(dx, dy)
			dx /= g
			dy /= g
			key := strconv.Itoa(dx) + " " + strconv.Itoa(dy)
			_, ok := m[key]
			if !ok {
				m[key] = 1
			}
			m[key]++
			max = utils.Max(max, m[key])
		}
	}
	return max
}