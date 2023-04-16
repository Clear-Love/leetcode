/*
 * @Author: lmio
 * @Date: 2023-04-16 14:40:09
 * @LastEditTime: 2023-04-16 17:45:51
 * @FilePath: /leetcode/code/1157.go
 * @Description:1157. 子数组中占绝大多数的元素
 */
package code

import (
	"math/rand"
	"sort"
)

type MajorityChecker struct {
	data []int
	m map[int][]int
}


func MajorityChecker_new(arr []int) MajorityChecker {
    loc := map[int][]int{}
    for i, x := range arr {
        loc[x] = append(loc[x], i)
    }
    return MajorityChecker{arr, loc}
}

func (mc *MajorityChecker) Query(left int, right int, threshold int) int {
	length := right - left + 1
    for i := 0; i < 20; i++ {
        x := mc.data[rand.Intn(right-left+1)+left]
        pos := mc.m[x]
        occ := sort.SearchInts(pos, right+1) - sort.SearchInts(pos, left)
        if occ >= threshold {
            return x
        }
		if occ*2 >= length {
			return -1
		}
    }
    return -1
}
