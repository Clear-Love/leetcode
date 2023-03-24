/*
 * @Author: lmio
 * @Date: 2023-03-24 21:06:06
 * @LastEditTime: 2023-03-24 21:13:15
 * @FilePath: /leetcode/offer/58.go
 * @Description:剑指 Offer 58 - II. 左旋转字符串
 */
package offer

func ReverseLeftWords(s string, n int) string {
	str := []byte(s)
	return string(append(str[n:], str[:n]...))
}