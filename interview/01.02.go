/*
 * @Author: lmio
 * @Date: 2023-04-10 23:31:29
 * @LastEditTime: 2023-04-10 23:35:21
 * @FilePath: /leetcode/interview/01.02.go
 * @Description:面试题 01.02. 判定是否互为字符重排
 */
package interview

func CheckPermutation(s1 string, s2 string) bool {
	code := make([]int, 26)
	if len(s1) != len(s2) {
		return false
	}
	for i := range s1 {
		code[s1[i]-'a']++
	}
	for i := range s2 {
		if code[s2[i]-'a'] <= 0 {
			return false
		}
		code[s2[i]-'a']--
	}
	return true
}