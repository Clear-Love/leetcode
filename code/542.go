/*
 * @Author: lmio
 * @Date: 2023-02-08 17:58:38
 * @LastEditTime: 2023-02-19 23:28:57
 * @FilePath: /leetcode/code/542.go
 * @Description:542.01矩阵
 */
package code

func UpdateMatrix(mat [][]int) [][]int {
    n, m := len(mat), len(mat[0])
    queue := make([][]int, 0)
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if mat[i][j] == 0 {
                queue = append(queue, []int{i, j})
            } else {
                mat[i][j] = -1
            }
        }
    }
	
    d := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

    for len(queue) > 0 {
        point := queue[0]
		x, y := point[0], point[1]
        queue = queue[1:] // 除去队列头
        for _, v := range d {
            _x := point[0] + v[0]
            _y := point[1] + v[1]
			// 访问未访问过的上下左右节点
            if _x >= 0 && _x < n && _y >= 0 && _y < m && mat[_x][_y] == -1 {
                mat[_x][_y] = mat[x][y] + 1
                queue = append(queue, []int{_x, _y})
            }
        }
    }
    
    return mat
}