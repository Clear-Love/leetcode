/*
 * @Author: lmio
 * @Date: 2023-04-07 09:52:42
 * @LastEditTime: 2023-04-07 14:29:39
 * @FilePath: /leetcode/utils/heap.go
 * @Description:堆结构
 */
package utils

// 自定义最大堆类型
type MaxHeap []int

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // 使用 ">" 实现最大堆
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

func (h *MaxHeap) Getarr() []int {
	return *h
}

// 自定义最小堆类型
type MinHeap []int

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } // 使用 ">" 实现最小堆
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[:n-1]
    return x
}

func (h *MinHeap) Getarr() []int {
	return *h
}