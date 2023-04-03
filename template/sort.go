/*
 * @Author: lmio
 * @Date: 2023-03-22 11:06:31
 * @LastEditTime: 2023-04-01 23:35:33
 * @FilePath: /leetcode/template/sort.go
 * @Description:排序
 */
package template

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
func InsertSortUp[T any](array []T, less func(i, j int) bool)[]T  {
    n := len(array)
    for i:=1;i<n;i++ {
        for j:=i;j>0 && less(i, j);j-- {
                array[j],array[j-1] = array[j-1],array[j]
        }    
    }
    return array
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