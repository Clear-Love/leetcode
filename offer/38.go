/*
 * @Author: lmio
 * @Date: 2023-04-20 15:33:41
 * @LastEditTime: 2023-04-20 16:04:59
 * @FilePath: /leetcode/offer/38.go
 * @Description:剑指 Offer 38. 字符串的排列
 */
package offer

import (
	"leetcode/utils"
	"sort"
)

func Permutation(s string) []string {
	bs := utils.ToBytes(s)
	res := []string{}
	ans := []byte{}
	visited := make([]bool, len(s))
	sort.Slice(bs, func(i, j int) bool {return bs[i] < bs[j]})
	var backtrace func(n int)
	backtrace = func(n int) {
		if n == len(s) {
			res = append(res, string(ans))
		}
		for i := n; i < len(bs); i++ {
			if bs[i] == bs[i-1] && !visited[i-1] {
				continue
			}
			visited[i] = true
			ans = append(ans, bs[i])
			backtrace(n+1)
			ans = ans[:len(ans)-1]
			visited[i] = false
		}
	}
	backtrace(0)
	return res
}