/*
 * @Author: lmio
 * @Date: 2023-04-10 22:56:21
 * @LastEditTime: 2023-04-10 23:02:11
 * @FilePath: /leetcode/interview/01.01.go
 * @Description:面试题 01.01. 判定字符是否唯一
 */
package interview

func IsUnique(astr string) bool {
	code := make([]bool, 26)
	if len(astr) > 26 {
		return false
	}
	for i := range astr {
		if code[astr[i]-'a'] {
			return false
		}
		code[astr[i]-'a'] = true
	}
	return true
}