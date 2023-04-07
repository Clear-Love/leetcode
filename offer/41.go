/*
 * @Author: lmio
 * @Date: 2023-04-07 10:11:54
 * @LastEditTime: 2023-04-07 14:30:24
 * @FilePath: /leetcode/offer/41.go
 * @Description:剑指 Offer 41. 数据流中的中位数
 */
package offer

import (
	. "leetcode/utils"
)

type MedianFinder struct {
	data []int
	Size int
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	return MedianFinder{[]int{}, 0}
}


func (this *MedianFinder) AddNum(num int)  {
	this.data = InsertSortarr(this.data, num)
	this.Size++
}


func (this *MedianFinder) FindMedian() float64 {
	arr := this.data
	l := this.Size
	if l == 0 {
		return 0.0
	}
	if l & 1 == 1 {
		// 奇数
		return float64(arr[l/2])
	}else {
		return (float64(arr[l/2-1]) + float64(arr[l/2])) / 2.0
	}
}