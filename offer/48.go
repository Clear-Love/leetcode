/*
 * @Author: lmio
 * @Date: 2023-04-01 14:23:18
 * @LastEditTime: 2023-04-01 14:45:43
 * @FilePath: /leetcode/offer/48.go
 * @Description:剑指 Offer 48. 最长不含重复字符的子字符串
 */
package offer

import "leetcode/template"

func LengthOfLongestSubstring(s string) int {
	sMap := map[byte]int{}
	max := 0
	start := 0
	for i := 0; i < len(s); i++ {
		ch := s[i]
		index, ok := sMap[ch]
		if ok {
			for j := start; j < index; j++ {
				delete(sMap, s[j])
			}
			start = index
		}else {
			max = template.Max(max, i-start+1)
		}
		sMap[ch] = i
	}
	return max
}