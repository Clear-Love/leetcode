/*
 * @Author: lmio
 * @Date: 2023-02-21 17:53:44
 * @LastEditTime: 2023-02-21 18:28:43
 * @FilePath: /leetcode/code/844.go
 * @Description:844.比较含退格的字符串
 */
package code

func BackspaceCompare(s, t string) bool {
	removePrecedingChar := func (s string) string {
		var slice []byte
		for i := 0; i < len(s); i++ {
			if s[i] == '#' {
				if len(slice) > 0 {
					// 删除前一个字符
					slice = slice[:len(slice)-1]
				}
			} else {
				// 将当前字符添加到切片中
				slice = append(slice, s[i])
			}
		}
		return string(slice)
	}
	s, t = removePrecedingChar(s), removePrecedingChar(t)
	return s == t
}