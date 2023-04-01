/*
 * @Author: lmio
 * @Date: 2023-04-01 18:08:45
 * @LastEditTime: 2023-04-01 18:46:31
 * @FilePath: /leetcode/code/17.go
 * @Description:17. 电话号码的字母组合
 */
package code

func LetterCombinations(digits string) []string {
	if len(digits) == 0 {
		return nil
	}
	phoneMap := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}
	res := []string{}
	ans := []byte{}
	var backbrack func(n int)
	backbrack = func(n int) {
		if n == len(digits) {
			res = append(res, string(ans))
			return
		}
		str := phoneMap[digits[n]]
		for _, ch := range str {
			ans = append(ans, byte(ch))
			backbrack(n+1)
			ans = ans[:len(ans)-1]
		}
	}
	return res
}