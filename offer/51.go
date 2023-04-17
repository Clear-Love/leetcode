/*
 * @Author: lmio
 * @Date: 2023-04-17 16:22:29
 * @LastEditTime: 2023-04-17 21:13:25
 * @FilePath: /leetcode/offer/51.go
 * @Description:剑指 Offer 51. 数组中的逆序对
 */
package offer

func ReversePairs(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	var mergeSort func([]int) int
	mergeSort = func(arr []int) int {
		n := len(arr)
		if n == 1 {
			return 0
		}
		larr, rarr := arr[:n/2], arr[n/2:]
		res := mergeSort(larr) + mergeSort(rarr)
		resarr := make([]int, 0, n)
		offset := 0
		for len(larr) > 0 && len(rarr) > 0 {
			if larr[0] <= rarr[0] {
				resarr = append(resarr, larr[0])
				larr = larr[1:]
				res += offset
			}else {
				offset++
				resarr = append(resarr, rarr[0])
				rarr = rarr[1:]
			}
		}
		if len(larr) == 0 {
			resarr = append(resarr, rarr...)
		}else {
			res += len(larr)*offset
			resarr = append(resarr, larr...)
		}
		copy(arr, resarr)
		return res
	}
	return mergeSort(nums)
}