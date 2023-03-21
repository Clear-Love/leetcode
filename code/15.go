/*
 * @Author: lmio
 * @Date: 2023-02-21 16:50:11
 * @LastEditTime: 2023-02-21 18:45:01
 * @FilePath: /leetcode/code/15.go
 * @Description:15.三数之和
 */
package code

import "sort"

func ThreeSum(nums []int) [][]int {
	sort.Ints(nums)
	length := len(nums)
	res := [][]int{}
	nextval := func(index *int) {
		val := nums[*index]
		for *index < length && nums[*index] == val {
			*index++
		}
	}
	prevval := func(index *int) {
		val := nums[*index]
		for *index > 0 && nums[*index] == val {
			*index--
		}
	}
	for i := 0; i < length-2 && nums[i] <= 0; nextval(&i) {
		j := i + 1
		k := length - 1
		for j < k {
			sum := nums[i] + nums[j] + nums[k]
			if sum == 0 {
				res = append(res, []int{nums[i], nums[j], nums[k]})
				nextval(&j)
				prevval(&k)
			} else if sum < 0 {
				j++
			} else {
				k--
			}
		}
	}
	return res
}
