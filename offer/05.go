/*
 * @Author: lmio
 * @Date: 2023-03-24 20:54:23
 * @LastEditTime: 2023-03-24 21:05:47
 * @FilePath: /leetcode/offer/05.go
 * @Description:剑指 Offer 05. 替换空格
 */
package offer

func ReplaceSpace(s string) string {
	res := make([]byte, len(s))
	for i := range s {
		if s[i] == ' ' {
			res = append(res, "%20"...)
		}else {
			res = append(res, s[i])
		}
	}
	return string(res)
}