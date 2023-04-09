/*
 * @Author: lmio
 * @Date: 2023-04-09 14:07:49
 * @LastEditTime: 2023-04-09 14:20:36
 * @FilePath: /leetcode/code/2399.go
 * @Description:2399. 检查相同字母间的距离
 */
package code

func CheckDistances(s string, distance []int) bool {
	dict := map[byte]int{}
	for i := range s {
		index, ok := dict[s[i]]
		if !ok {
			dict[s[i]] = i
			continue
		}
		if i-index-1 != distance[s[i]-'a'] {
			return false
		}
	}
	return true
}