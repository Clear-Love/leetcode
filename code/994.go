/*
 * @Author: lmio
 * @Date: 2023-02-08 21:52:45
 * @LastEditTime: 2023-02-19 23:36:26
 * @FilePath: /leetcode/code/994.go
 * @Description:994.腐烂的橘子
 */
package code

func OrangesRotting(grid [][]int) int {
	queue := make([][]int, 0)
	n, m := len(grid), len(grid[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, []int{i, j})
			}
		}
	}

	d := [][]int{{0,1}, {0,-1}, {1,0}, {-1,0},}

	newQueue := make([][]int, 0)
	ans := 0

	for len(queue) > 0 {
		x, y := queue[0][0], queue[0][1]
		queue = queue[1:]
		for _, val := range d {
			_x, _y := x+val[0], y+val[1]
			if(_x >=0 && _x < n && _y >= 0 && _y < m) {
				if grid[_x][_y] == 1 {
					grid[_x][_y] = 2
					newQueue = append(newQueue, []int{_x, _y})
				}
			}
		}
		if len(queue) == 0 {
			newQueue, queue = queue, newQueue
			if len(queue) > 0 {
				ans++
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 1 {
				return -1
			}
		}
	}
	return ans
}