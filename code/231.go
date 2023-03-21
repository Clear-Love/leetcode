/*
 * @Author: lmio
 * @Date: 2023-02-12 20:41:15
 * @LastEditTime: 2023-02-19 23:28:34
 * @FilePath: /leetcode/code/231.go
 * @Description:231.2的幂
 */
package code

func IsPowerOfTwo(n int) bool {
	return n > 0 && n&(n-1) == n 
}