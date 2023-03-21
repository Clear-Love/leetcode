/*
 * @Author: lmio
 * @Date: 2023-02-21 22:35:35
 * @LastEditTime: 2023-02-22 12:09:23
 * @FilePath: /leetcode/code/438.go
 * @Description:438.找到字符串中所有字母异位词
 */
package code

func FindAnagrams(s, p string) []int {
	if len(s) < len(p) {
		return nil
	}
    cnt := [26]int{}
    for _, ch := range p {
        cnt[ch - 'a']--
    }
	res := []int{}
    left := 0
    for right, ch := range s {
        index := ch - 'a'
        cnt[index]++
        for cnt[index] > 0 {
            cnt[s[left] - 'a']--
            left++
        }
        if right - left + 1 == len(p) {
            res = append(res, left) 
        }
    }
    return res
}