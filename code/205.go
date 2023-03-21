/*
 * @Author: lmio
 * @Date: 2023-02-13 23:52:18
 * @LastEditTime: 2023-02-19 23:28:22
 * @FilePath: /leetcode/code/205.go
 * @Description:205.同构字符串
 */
package code

func IsIsomorphic(s string, t string) bool {
	sTt := map[byte]byte{}
	for i := range t {
		ch := t[i]
		val, ok := sTt[ch]
		if ok {
			if val != ch {
				return false
			}
		}else {
			sTt[ch] = s[i]
		}
	}
	return true
}