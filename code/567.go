/*
 * @Author: lmio
 * @Date: 2023-02-05 23:56:17
 * @LastEditTime: 2023-02-19 23:29:10
 * @FilePath: /leetcode/code/567.go
 * @Description:567.字符串的排列
 */
package code

func CheckInclusion(s1, s2 string) bool {
    l1, l2 := len(s1), len(s2)
    if l1 > l2 {
        return false
    }
    cnt := [26]int{}
    for _, ch := range s1 {
        cnt[ch - 'a']--
    }

    left := 0
    for right, ch := range s2 {
        index := ch - 'a'
        cnt[index]++
        for cnt[index] > 0 {
            cnt[s2[left] - 'a']--
            left++
        }
        if right - left + 1 == l1 {
            return true
        }
    }
    return false
}