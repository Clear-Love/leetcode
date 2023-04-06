/*
 * @Author: lmio
 * @Date: 2023-04-06 08:16:37
 * @LastEditTime: 2023-04-06 09:07:22
 * @FilePath: /leetcode/offer/45.go
 * @Description:面试题45. 把数组排成最小的数
 */
package offer

import (
	"fmt"
	"leetcode/template"
	"sort"
	"strconv"
)

func MinNumber(nums []int) string {
	sort.Slice(nums, func(i, j int) bool {
		x := fmt.Sprintf("%d%d", nums[i], nums[j])
        y := fmt.Sprintf("%d%d", nums[j], nums[i])
        return x < y
	})
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[0] = nums[0], nums[i]
			break
		}
	}
	res := []byte{}
	for _, val := range nums {
		str := strconv.Itoa(val)
		res = append(res, str...)
	}
	return template.ToString(res)
}