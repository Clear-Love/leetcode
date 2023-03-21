/*
 * @Author: lmio
 * @Date: 2023-02-21 18:46:04
 * @LastEditTime: 2023-02-21 20:12:13
 * @FilePath: /leetcode/code/986.go
 * @Description:986.区间列表的交集
 */
package code

import "leetcode/template"

func IntervalIntersection(firstList, secondList [][]int) [][]int {
	res := [][]int{}
	for i := range firstList {
		for j := range secondList {
			if firstList[i][1] < secondList[j][0] {
				break
			}
			section := template.FindIntersection(firstList[i], secondList[j])
			if  section != nil {
				res = append(res, section)
			}
		}
	}
	return res
}