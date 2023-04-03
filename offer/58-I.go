/*
 * @Author: lmio
 * @Date: 2023-04-03 09:59:17
 * @LastEditTime: 2023-04-03 10:13:47
 * @FilePath: /leetcode/offer/58-I.go
 * @Description:剑指 Offer 58 - I. 翻转单词顺序
 */
package offer

import (
	"regexp"
	"sort"
	"strings"
)

func ReverseWords(s string) string {
	words := regexp.MustCompile(`\s+`).Split(strings.Trim(s, " "), -1)
	sort.SliceStable(words, func(i, j int) bool {
		return true
	})
	return strings.Join(words, " ")
}