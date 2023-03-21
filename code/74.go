/*
 * @Author: lmio
 * @Date: 2023-02-13 23:29:36
 * @LastEditTime: 2023-02-19 23:27:06
 * @FilePath: /leetcode/code/74.go
 * @Description:74.搜索二维矩阵
 */
package code

func SearchMatrix(matrix [][]int, target int) bool {
	n, m := len(matrix), len(matrix[0])
	left, right := 0, n*m - 1
	i, j := 0, 0
	for left <= right {
		mid := (left + right) >> 1
		i, j = mid / m, mid % m
		if matrix[i][j] == target {
			return true
		}else if matrix[i][j] < target {
			left = mid + 1
		}else {
			right = mid - 1
		}
	}
	return false
}