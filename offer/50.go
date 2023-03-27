/*
 * @Author: lmio
 * @Date: 2023-03-27 17:40:40
 * @LastEditTime: 2023-03-27 17:59:06
 * @FilePath: /leetcode/offer/50.go
 * @Description:剑指 Offer 50. 第一个只出现一次的字符
 */
package offer

func FinstUniqChar(s string) byte {
	onces := map[byte]int{}
	for i := range s {
		_, ok := onces[s[i]]
		if ok {
			onces[s[i]] = -1
		}else {
			onces[s[i]] = i
		}
	}
	res := byte(' ')
	min := len(s)
	for ch, index := range onces {
		if index != -1 && index < min {
			min = index
			res = ch
		}
	}
	return res
}