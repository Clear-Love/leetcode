/*
 * @Author: lmio
 * @Date: 2023-03-22 16:37:17
 * @LastEditTime: 2023-03-22 16:58:22
 * @FilePath: /leetcode/offer/30.go
 * @Description:剑指 Offer 30. 包含min函数的栈
 */
package offer

type MinStack struct {
	datastack []int
	minstack []int
}


/** initialize your data structure here. */
func newMinstack() MinStack {
	return MinStack{
		[]int{},
		[]int{},
	}
}


func (this *MinStack) Push(x int)  {
	this.datastack = append(this.datastack, x)
	if len(this.minstack) == 0 || this.minstack[len(this.minstack)-1] >= x {
		this.minstack = append(this.minstack, x)
	}
}


func (this *MinStack) Pop()  {
	val := this.datastack[len(this.datastack)-1]
	this.datastack = this.datastack[:len(this.datastack)-1]
	if this.minstack[len(this.minstack)-1] == val {
		this.minstack = this.minstack[:len(this.minstack)-1]
	}
}


func (this *MinStack) Top() int {
	return this.datastack[len(this.datastack)-1]
}


func (this *MinStack) Min() int {
	return this.minstack[len(this.minstack)-1]
}