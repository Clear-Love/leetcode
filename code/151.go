/*
 * @Author: lmio
 * @Date: 2023-04-03 10:17:40
 * @LastEditTime: 2023-04-07 14:33:22
 * @FilePath: /leetcode/code/151.go
 * @Description:151. 反转字符串中的单词
 */
package code

import (
	."leetcode/utils"
	"strings"
)

func ReverseWords(s string) string {
	res := make([]byte, 0, len(s))
	left := len(s)-1
	right := left
	for left >= 0 {
		for left >= 0 && s[left] == ' ' {
			left--
		}
		right = left
		for left >= 0 && s[left] != ' ' {
			left--
		}
		res = append(res, s[left+1:right+1]...)
		res = append(res, ' ')
	}
	return strings.Trim(ToString(res), " ")
}