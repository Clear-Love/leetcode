/*
 * @Author: lmio
 * @Date: 2023-04-01 18:58:23
 * @LastEditTime: 2023-04-01 20:18:17
 * @FilePath: /leetcode/code/79.go
 * @Description:79. 单词搜索
 */
package code

func Exist(board [][]byte, word string) bool {
	n, m := len(board), len(board[0])
	var backbrack func(x, y, n int) bool
	visited := make([][]bool, n)
	for i := 0; i < n; i++ {
		visited[i] = make([]bool, m)
	}
	move := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	backbrack = func(x, y, k int) bool {
		if word[k] != board[x][y] {
			return false
		}
		if k == len(word)-1 {
			return true
		}
		visited[x][y] = true
		for _, pos := range move {
			_x, _y := x + pos[0], y + pos[1]
			if !visited[x][y] && _x >= 0 && _x < n && _y >= 0 && _y < m && backbrack(_x, _y, k+1) {
				return true
			}
		}
		visited[x][y] = false
		return false
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if backbrack(i, j, 0) {
				return true
			}
		}
	}
	return false
}