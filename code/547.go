/*
 * @Author: lmio
 * @Date: 2023-02-22 22:12:24
 * @LastEditTime: 2023-02-22 22:22:40
 * @FilePath: /leetcode/code/547.go
 * @Description:547.省份数量
 */
package code

func FindCircleNum(isConnected [][]int) int {
	n, m := len(isConnected), len(isConnected[0])
	res := 0
	var dfs func (x, y int)
	dfs = func (x, y int)  {
		if isConnected[x][y] != 1 {
			return
		}
		isConnected[x][y] = 0
		for i := 0; i < m; i++ {
			dfs(y, i)
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if isConnected[i][j] == 1 {
				res++
				dfs(i, j)
			}
		}
	}
	return res
}