/*
 * @Author: lmio
 * @Date: 2023-02-05 23:16:07
 * @LastEditTime: 2023-02-19 23:26:03
 * @FilePath: /leetcode/code/3.go
 * @Description:3.无重复字符的最长子串
 */
package code

func LengthOfLongestSubstring(s string) int {
	length := len(s)
	if length < 2 {
		return length
	}
	left := 0
	right := 1
	max := 1
	for right < length {
		for i := left; i < right; i++ {
			if s[i] == s[right] {
				left = i + 1
				break
			}
		}
		right++
		subSize := right - left
		if subSize > max {
			max = subSize
		}
	}
	return max
}