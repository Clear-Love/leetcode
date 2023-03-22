/*
 * @Author: lmio
 * @Date: 2023-03-21 23:11:30
 * @LastEditTime: 2023-03-22 15:05:48
 * @FilePath: /leetcode/code/2423.go
 * @Description:2423.删除字符使频率相同
 */
package code

func EqualFrequency(word string) bool {
	freq := make(map[rune]int)
	for _, ch := range word {
		freq[ch] =freq[ch] + 1
	}
	values := make([]int, 0, len(word))
    for _, v := range freq {
        values = append(values, v)
    }
	for i := 0; i < len(values); i++ {
		values[i]--
		if CheckFrequency(values) {
			return true
		}
		values[i]++
	}
	return false
}

/**
 * @description: 检查数组中非0元素是否全部相等
 * @param {[]int} a
 * @return {*}
 */
func CheckFrequency(a []int) bool {
	pre := -1
	for  i := 0; i < len(a); i++ {
		if pre == -1 && a[i] != 0 {
			pre = a[i]
		}
		if a[i] != 0 && a[i] != pre {
			return false
		}
	}
	return true
}