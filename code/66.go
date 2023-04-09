/*
 * @Author: lmio
 * @Date: 2023-04-09 15:48:36
 * @LastEditTime: 2023-04-09 16:08:42
 * @FilePath: /leetcode/code/66.go
 * @Description:66. 加一
 */
package code

func PlusOne(digits []int) []int {
	res := make([]int, len(digits)+1)
	array := 1
	j := len(digits)
	for i := len(digits)-1; i >= 0; i-- {
		num := digits[i]+array
		res[j] = num % 10
		array = num / 10
		j--
	}
	if array == 0 {
		return res[1:]
	}
	res[0] = array
	return res
}