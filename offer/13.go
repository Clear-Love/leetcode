/*
 * @Author: lmio
 * @Date: 2023-04-04 08:29:41
 * @LastEditTime: 2023-04-04 09:05:29
 * @FilePath: /leetcode/offer/13.go
 * @Description:面试题13. 机器人的运动范围
 */
package offer

/**
 * @description: 广度优先搜索
 * @param {*} m
 * @param {*} n
 * @param {int} k
 * @return {*}
 */
func MovingCount(m, n, k int) int {
	Numsum := func (num int) (sum int) {
		for num != 0 {
			sum += num%10
			num /= 10
		}
		return
	}
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	nodes := [][2]int{{0, 0}}
	move := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	res := 1
	visited[0][0] = true
	for len(nodes) != 0 {
		node := nodes[0]
		nodes = nodes[1:]
		_x, _y := node[0], node[1]
		for _, pos := range move {
			x := _x + pos[0]
			y := _y + pos[1]
			if x >= 0 && y >= 0 && x < m && y < n && !visited[x][y] && Numsum(x)+ Numsum(y) <= k {
				visited[x][y] = true			
				res++
				nodes = append(nodes, [2]int{x, y})		
			}
		}
	}
	return res
}