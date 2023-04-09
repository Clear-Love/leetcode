/*
 * @Author: lmio
 * @Date: 2023-03-22 11:06:31
 * @LastEditTime: 2023-04-09 17:06:18
 * @FilePath: /leetcode/utils/sort.go
 * @Description:排序
 */
package utils

import "sort"

func SortMapValues(m map[any]int) []int {
    values := make([]int, 0, len(m))
    for _, v := range m {
        values = append(values, v)
    }
    sort.Ints(values)
    return values
}


/**
 * @description: 插入排序,适用于数组基本有序的情况
 * @param {[]int} array
 * @return {*}
 */
func InsertSortUp[T comparable](array []T, less func(i, j int) bool)[]T  {
    n := len(array)
    for i:=1;i<n;i++ {
        for j:=i;j>0 && less(i, j);j-- {
                array[j],array[j-1] = array[j-1],array[j]
        }    
    }
    return array
}

func InsertSortarr[T int|int64|float32|float64](arr []T, num T) []T {
    // 找到插入位置 即找到大于目标值的第一个数
    l, r := 0, len(arr)
    for l < r {
        mid := (l + r) >> 1
        if arr[mid] < num {
            l = mid + 1
        }else {
            r = mid
        }
    }

    // 检查是否插入到末尾
    if l == len(arr) {
        // 直接将新元素添加到末尾
        arr = append(arr, num)
    } else {
        // 将插入位置后的元素都向后移动一位
        arr = append(arr[:l+1], arr[l:]...)

        // 插入新元素
        arr[l] = num
    }
    return arr
}


/**
 * @description: 桶排序，适用与数据量大且数据范围不大
 * @param {[]int} arr
 * @param {int} maxVal
 * @return {*}
 */
func BucketSort(arr []int, maxVal int) []int {
    // 创建桶
    bucket := make([]int, maxVal+1)
    // 计数每个元素的个数，放入桶中
    for _, val := range arr {
        bucket[val]++
    }
    // 将桶中的元素按顺序放回原数组中
    k := 0
    for i := 0; i <= maxVal; i++ {
        for j := 0; j < bucket[i]; j++ {
            arr[k] = i
            k++
        }
    }
    return arr
}

func ReverseSlice[T any](s []T) {
	length := len(s)
	left := 0
	right := length - 1

	for left < right {
		// 交换左右指针所指向的元素
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}