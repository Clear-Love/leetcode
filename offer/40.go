/*
 * @Author: lmio
 * @Date: 2023-04-07 09:43:52
 * @LastEditTime: 2023-04-07 14:30:33
 * @FilePath: /leetcode/offer/40.go
 * @Description:剑指 Offer 40. 最小的k个数
 */
package offer

import (
	"container/heap"
	."leetcode/utils"
)

func GetLeastNumbers(arr []int, k int) []int {
	maxheap := &MaxHeap{}
	for i := 0; i < k; i++ {
		heap.Push(maxheap, arr[i])
	}
	for i := k; i < len(arr); i++ {
		heap.Push(maxheap, arr[i])
		heap.Pop(maxheap)
	}
	return maxheap.Getarr()
}