/*
 * @Author: lmio
 * @Date: 2023-04-14 10:54:54
 * @LastEditTime: 2023-04-14 11:41:55
 * @FilePath: /leetcode/offer/57-II.go
 * @Description:剑指 Offer 57 - II. 和为s的连续正数序列
 */
package offer

func FindContinuouSequence(target int) [][]int {
	res := [][]int{}
	addres := func(i, j int) {
		arr := make([]int, j-i+1)
		for i <= j {
			arr = append(arr, i)
			i++
		}
		res = append(res, arr)
	}
	for i := 1; i <= target/2; i++ {
		l, r := i, target-1
		for l < r{
			mid := (l+r)/2
			sum := ((i+mid)*(mid-i+1))/2
			if sum == target {
				addres(i, mid)
			}
			if sum < target {
				l = mid+1
			}else {
				r = mid
			}
		}
	}
	return res
}