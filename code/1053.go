/*
 * @Author: lmio
 * @Date: 2023-04-03 21:30:31
 * @LastEditTime: 2024-05-21 15:14:54
 * @FilePath: /leetcode/code/1053.go
 * @Description:1053. 交换一次的先前排列
 */
package code

func PrevPermOpt1(arr []int) []int {
	for i := len(arr) - 2; i >= 0; i-- {
		for j := i + 1; j < len(arr); j++ {
			if arr[j] < arr[i] {
				index := j
				for k := j + 1; k < len(arr); k++ {
					if arr[k] < arr[i] && arr[k] > arr[index] {
						index = k
					}
				}
				arr[i], arr[index] = arr[index], arr[i]
				return arr
			}
		}
	}
	return arr
}
