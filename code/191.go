/*
 * @Author: lmio
 * @Date: 2023-02-12 20:50:01
 * @LastEditTime: 2023-02-12 20:58:13
 * @FilePath: /leetcode/code/191.go
 * @Description:191.位1的个数
 */
package code

func HammingWeight(num uint32) int {
	res := 0
	for num != 0 {
		if num & 1 == 1 {
			res++
		}
		num = num >> 1
	}
	return res
}