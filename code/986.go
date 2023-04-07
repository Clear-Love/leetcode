/*
 * @Author: lmio
 * @Date: 2023-02-21 18:46:04
 * @LastEditTime: 2023-04-07 14:37:46
 * @FilePath: /leetcode/code/986.go
 * @Description:986.区间列表的交集
 */
package code

import "leetcode/utils"

func IntervalIntersection(firstList, secondList [][]int) [][]int {
	res := [][]int{}
	for i := range firstList {
		for j := range secondList {
			if firstList[i][1] < secondList[j][0] {
				break
			}
			section := utils.FindIntersection(firstList[i], secondList[j])
			if  section != nil {
				res = append(res, section)
			}
		}
	}
	return res
}