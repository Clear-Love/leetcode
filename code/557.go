/*
 * @Author: lmio
 * @Date: 2023-02-05 17:03:52
 * @LastEditTime: 2023-02-19 23:29:03
 * @FilePath: /leetcode/code/557.go
 * @Description:557.反转字符串中的单词
 */
package code

import "strings"

func ReverseWords(s string) string {
	reverseString := func (s []byte) []byte{
	left := 0
	right := len(s)-1
	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
	return s
}
	res := strings.Split(s, " ")
	for key, val := range res{
		res[key] = string(reverseString([]byte(val)))
	}
	return strings.Join(res, " ")
}

