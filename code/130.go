/*
 * @Author: lmio
 * @Date: 2023-03-29 20:15:17
 * @LastEditTime: 2023-03-29 21:48:30
 * @FilePath: /leetcode/code/130.go
 * @Description:130. 被围绕的区域
 */
package code

func Solve(board [][]byte) {
	n, m := len(board), len(board[0])
	type Posit struct {
		X int
		Y int
	}
	posits := []Posit{}
	for i := 0; i < n; i++ {
		if board[i][0] == 'O' {
			posits = append(posits, Posit{i, 0})
		}
		if board[i][m-1] == 'O' {
			posits = append(posits, Posit{i, m-1})
		}
	}
	for j := 1; j < m-1; j++ {
		if board[0][j] == 'O' {
			posits = append(posits, Posit{0, j})
		}
		if board[n-1][j] == 'O' {
			posits = append(posits, Posit{n-1, j})
		}
	}
	
	move := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(posits) != 0 {
		pos := posits[0]
		posits = posits[1:]
		// 标记
		board[pos.X][pos.Y] = '1'
		for _, d := range move {
			x, y := pos.X + d[0], pos.Y + d[1]
			if x >= 0 && y >= 0 && x < n && y < m && board[x][y] == 'O' {
				posits = append(posits, Posit{x, y})
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] == 'O' {
				board[i][j] = 'X'
			}else if board[i][j] == '1' {
				board[i][j] = 'O'
			}
		}
	}
}