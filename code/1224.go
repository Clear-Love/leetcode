/*
 * @Author: lmio
 * @Date: 2023-03-22 15:07:19
 * @LastEditTime: 2023-03-22 16:00:46
 * @FilePath: /leetcode/code/1224.go
 * @Description:1224.最大相等频率
 */
package code

import "leetcode/template"

func MaxEqualFreq(nums []int) int {
	cnts := map[int]int{}
	cntsNum := map[int]int{}
	maxCnt := 0
	ans := 0
	for i, v := range nums {
		if cnts[v] > 0 {
			cntsNum[cnts[v]]--
		}
		cnts[v]++
		cntsNum[cnts[v]]++
		maxCnt = template.Max(cnts[v], maxCnt)
		if maxCnt == 1 ||
			cntsNum[maxCnt] == 1 && cntsNum[maxCnt-1]*(maxCnt-1) + maxCnt == i+1 ||
			cntsNum[1] == 1 && cntsNum[maxCnt]*maxCnt+1 == i+1 {
				ans = i+1
			}
	}
	return ans
}