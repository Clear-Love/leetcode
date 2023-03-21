/*
 * @Author: lmio
 * @Date: 2023-02-10 19:20:29
 * @LastEditTime: 2023-02-19 23:36:05
 * @FilePath: /leetcode/code/784.go
 * @Description:784.字母大小写全排列
 */
package code

import "unicode"

func LetterCasePermutation(s string) []string {
	ans := []string{}
	l := len(s)
	var backtrace func(str []rune, k int)
	backtrace = func(str []rune, k int) {
		if k == l {
			ans = append(ans, string(str))
			return
		}
		if !unicode.IsLetter(str[k]) {
			backtrace(str, k+1)
			return
		}
		backtrace(str, k+1)
		str[k] ^= 32
		backtrace(str, k+1)
		str[k] ^= 32
	}
	backtrace([]rune(s), 0)
	return ans
}