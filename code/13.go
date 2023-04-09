/*
 * @Author: lmio
 * @Date: 2023-04-09 14:22:42
 * @LastEditTime: 2023-04-09 15:13:20
 * @FilePath: /leetcode/code/13.go
 * @Description:13. 罗马数字转整数
 */
package code

func RomanToInt(s string) int {
	res := 0
	romans := map[byte]int{
		'M': 1000,
		'D': 500,
		'C': 100,
		'L': 50,
		'X': 10,
		'V': 5,
		'I': 1,
	}
	for i := 0; i < len(s); i++ {
		if i == len(s)-1 {
			res += romans[s[i]]
			break
		}
		switch s[i] {
			case 'I':
				if s[i+1] == 'V'{
					res += 4
					i++
				}else if s[i+1] == 'X' {
					res += 9
					i++
				}else {
					res += romans[s[i]]
				}
			case 'X':
				if s[i+1] == 'L'{
					res += 40
					i++
				}else if s[i+1] == 'C' {
					res += 90
					i++
				}else {
					res += romans[s[i]]
				}
			case 'C':
				if s[i+1] == 'D'{
					res += 400
					i++
				}else if s[i+1] == 'M' {
					res += 900
					i++
				}else {
					res += romans[s[i]]
				}
			default:
				res += romans[s[i]]
		}
		
	}
	return res
}