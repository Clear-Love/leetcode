/*
 * @Author: lmio
 * @Date: 2023-03-22 16:07:35
 * @LastEditTime: 2023-03-22 16:38:00
 * @FilePath: /leetcode/offer/09.go
 * @Description:剑指 Offer 09. 用两个栈实现队列
 */
package offer

type CQueue struct {
	instack, outstack []int
}


func NewCQeue() CQueue {
	return CQueue{
		[]int{},
		[]int{},
	}
}


func (this *CQueue) AppendTail(value int)  {
	this.instack = append(this.instack, value)
}


func (this *CQueue) DeleteHead() int {
	if len(this.outstack) == 0 {
		if len(this.instack) == 0 {
			return -1
		}
		for len(this.instack) > 0 {
			this.outstack = append(this.outstack, this.instack[len(this.instack)-1])
			this.instack = this.instack[:len(this.instack)-1]
		}
	}
	res := this.outstack[len(this.outstack)-1]
	this.outstack = this.outstack[:len(this.outstack)-1]
	return res
}
