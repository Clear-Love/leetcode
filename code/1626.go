/*
 * @Author: lmio
 * @Date: 2023-03-22 18:48:08
 * @LastEditTime: 2023-03-22 20:27:29
 * @FilePath: /leetcode/code/1626.go
 * @Description:1626.无矛盾的最佳球队
 */
package code

import (
	"leetcode/template"
	"sort"
)

func BestTeamScore(scores []int, ages []int) int {
	n := len(scores)
	player := make([][]int, n)
	for i := range scores {
		player[i] = []int{scores[i], ages[i]}
	}

	// 按成绩升序排序，若成绩相同，按年龄升序排序
	sort.Slice(player, func(i, j int) bool {
		if player[i][0] < player[j][0] {
			return true
		}else if player[i][0] > player[j][0] {
			return false
		}
		return player[i][1] < player[j][1]
	})

	dp := make([]int, n)
	dp[0] = player[0][0]

	res := dp[0]
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if player[j][1] <= player[i][1] {
				dp[i] = template.Max(dp[i], dp[j])
			}
		}
		dp[i] += player[i][0]
		res = template.Max(res, dp[i])
	}
	return res
}