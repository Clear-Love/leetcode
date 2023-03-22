/*
 * @Author: lmio
 * @Date: 2023-03-22 11:06:31
 * @LastEditTime: 2023-03-22 14:21:31
 * @FilePath: /leetcode/template/sort.go
 * @Description:排序
 */
package template

import "sort"

func SortMapValues(m map[rune]int) []int {
    values := make([]int, 0, len(m))
    for _, v := range m {
        values = append(values, v)
    }
    sort.Ints(values)
    return values
}


/**
 * @description: 插入排序，从小到大 适用于数组基本有序的情况
 * @param {[]int} array
 * @return {*}
 */
func InsertSortUp(array []int)[]int  {
    n := len(array)
    for i:=1;i<n;i++ {
        for j:=i;j>0 && array[j] < array[j-1];j-- {
                array[j],array[j-1] = array[j-1],array[j]
        }    
    }
    return array
}


/**
 * @description: 插入排序，从大到小
 * @param {[]int} array
 * @return {*}
 */
func InsertSortDown(array []int)[]int  {
    n := len(array)
    for i:=1;i<n;i++ {
        for j:=i;j>0 && array[j] > array[j-1];j-- {
                array[j],array[j-1] = array[j-1],array[j]
        }    
    }
    return array
}