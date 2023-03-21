/*
 * @Author: lmio
 * @Date: 2023-02-05 16:38:22
 * @LastEditTime: 2023-02-19 23:28:52
 * @FilePath: /leetcode/code/344.go
 * @Description:344.反转字符串
 */
package code

func ReverseString(s []byte){
	left := 0
	right := len(s)-1
	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}