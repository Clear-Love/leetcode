/*
 * @Author: lmio
 * @Date: 2023-04-07 09:52:42
 * @LastEditTime: 2023-04-19 10:59:30
 * @FilePath: /leetcode/utils/heap.go
 * @Description:堆结构
 */
package utils

// 自定义最大堆类型
type MaxHeap[T Number] struct {
    Slice []T
}

func (h *MaxHeap[T]) Len() int { return len(h.Slice) }
func (h *MaxHeap[T]) Less(i, j int) bool { return h.Slice[i] > h.Slice[j] } // 使用 ">" 实现最大堆
func (h *MaxHeap[T]) Swap(i, j int) { h.Slice[i], h.Slice[j] = h.Slice[j], h.Slice[i] }

func (h *MaxHeap[T]) Push(x interface{}) {
    h.Slice = append(h.Slice, x.(T))
}

func (h *MaxHeap[T]) Pop() interface{} {
    n := len(h.Slice)
    x := (h.Slice)[n-1]
    h.Slice = (h.Slice)[:n-1]
    return x
}

// 自定义最小堆类型
type MinHeap[T Number] struct {
    Slice []T
}

func (h MinHeap[T]) Len() int { return len(h.Slice) }
func (h MinHeap[T]) Less(i, j int) bool { return h.Slice[i] < h.Slice[j] } // 使用 ">" 实现最小堆
func (h *MinHeap[T]) Swap(i, j int) { h.Slice[i], h.Slice[j] = h.Slice[j], h.Slice[i] }

func (h *MinHeap[T]) Push(x interface{}) {
    h.Slice = append(h.Slice, x.(T))
}

func (h *MinHeap[T]) Pop() interface{} {
    n := len(h.Slice)
    x := h.Slice[n-1]
    h.Slice = h.Slice[:n-1]
    return x
}