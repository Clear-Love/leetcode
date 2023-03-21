/*
 * @Author: lmio
 * @Date: 2023-02-06 23:07:20
 * @LastEditTime: 2023-02-19 23:35:59
 * @FilePath: /leetcode/code/733.go
 * @Description:733.图像渲染
 */
package code


func FloodFill(image [][]int, sr int, sc int, color int) [][]int {
	dx := []int{1, 0, 0, -1}
    dy := []int{0, 1, -1, 0}
	var dfs func (image [][]int, x, y, currcolor, color int)
	dfs = func(image [][]int, x int, y int, currcolor int, color int) {
		if image[x][y] == currcolor {
			n, m := len(image[y]), len(image)
			image[x][y] = color
			for i := 0; i < 4; i++ {
				_x, _y := x+dx[i], y+dy[i]
				if _x >= 0 && x < n && _y >= 0 && _y < m {
					dfs(image, _x, _y, currcolor, color)
				}
			}
		}
	}
	currcolor := image[sr][sc]
	if currcolor != color {
		dfs(image, sr, sc, currcolor, color)
	}
	return image
}

