/*
 * @Author: lmio
 * @Date: 2023-04-19 15:32:22
 * @LastEditTime: 2023-04-19 15:48:58
 * @FilePath: /leetcode/offer/59-II.go
 * @Description:剑指 Offer 59 - II. 队列的最大值
 */
package offer

type MaxQueue struct {
	q []int
	maxstack []int
}


func MaxQueue_new() MaxQueue {
	return MaxQueue{[]int{}, []int{}}
}


func (mq *MaxQueue) Max_value() int {
	return mq.maxstack[0]
}


func (mq *MaxQueue) Push_back(value int)  {
	mq.q = append(mq.q, value)
	i := len(mq.maxstack)-1
	for i >=0 && mq.maxstack[i] < value {
		mq.maxstack = mq.maxstack[:i]
		i--
	}
	mq.maxstack = append(mq.maxstack, value)
}


func (mq *MaxQueue) Pop_front() int {
	if len(mq.q) == 0 {
		return -1
	}
	res := mq.q[0]
	mq.q = mq.q[1:]
	if mq.maxstack[0] == res {
		mq.maxstack = mq.maxstack[1:]
	}
	return res
}
