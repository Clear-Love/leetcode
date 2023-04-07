/*
 * @Author: lmio
 * @Date: 2023-03-27 17:28:06
 * @LastEditTime: 2023-04-07 14:30:41
 * @FilePath: /leetcode/offer/04.go
 * @Description:剑指 Offer 04. 二维数组中的查找
 */
package offer

import "leetcode/utils"

func FindNumberIn2DArray(matrix [][]int, target int) bool {
	if len(matrix) == 0 {
		return false
	}
	if len(matrix[0]) == 0 {
		return false
	}
	for i := range matrix {
		if matrix[i][0] > target {
			return false
		}
		if utils.Search_left(matrix[i], target) != -1 {
			return true
		}
	}
	return false
}