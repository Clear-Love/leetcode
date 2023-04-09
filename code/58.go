/*
 * @Author: lmio
 * @Date: 2023-04-09 15:40:22
 * @LastEditTime: 2023-04-09 15:47:16
 * @FilePath: /leetcode/code/58.go
 * @Description:58. 最后一个单词的长度
 */
package code

func LengthOfLastWord(s string) int {
	res := 0
	i := len(s)-1
	for i >=0 && s[i] == ' ' {
		i--
	}
	for i>= 0 && s[i] != ' ' {
		res++
		i--
	}
	return res
}