/*
 * @Author: lmio
 * @Date: 2023-04-15 14:00:08
 * @LastEditTime: 2023-04-15 15:44:04
 * @FilePath: /leetcode/offer/29.go
 * @Description:剑指 Offer 29. 顺时针打印矩阵
 */
package offer

func SpiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	left, right, top, bottom := 0, len(matrix[0])-1, 0, len(matrix)-1
	res := make([]int, 0, (right+1)*(bottom+1))
	for {
		// 从左到右
		for i := left; i <= right; i++ {
			res = append(res, matrix[top][i])
		}
		top++
		if top > bottom {
			break
		}
		// 从上到下
		for i := top; i <= bottom; i++ {
			res = append(res, matrix[i][right])
		}
		right--
		if left > right {
			break
		}
		// 从右到左
		for i := right; i >= left; i-- {
			res = append(res, matrix[bottom][i])
		}
		bottom--
		if top > bottom {
			break
		}
		// 从下到上
		for i := bottom; i >= top; i-- {
			res = append(res, matrix[i][left])
		}
		left++
		if left > right {
			break
		}
	}
	return res
}