/*
 * @Author: lmio
 * @Date: 2023-04-10 09:03:53
 * @LastEditTime: 2023-04-10 10:06:48
 * @FilePath: /leetcode/code/384.go
 * @Description:384. 打乱数组
 */
package code

import (
	"math/rand"
	"time"
)

type Solution struct {
	Array []int
	socure []int
	Size int
}


func Constructor(nums []int) Solution {
	return Solution{Array: nums, socure: append([]int{}, nums...), Size: len(nums)}
}


func (this *Solution) Reset() []int {
	return this.socure
}


func (this *Solution) Shuffle() []int {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := 0; i < this.Size-1; i++ {
		index := i + r.Intn(this.Size-i)
		this.Array[i], this.Array[index] = this.Array[index], this.Array[i]
	}
	return this.Array
}