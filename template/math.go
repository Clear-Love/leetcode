/*
 * @Author: lmio
 * @Date: 2023-02-19 23:30:39
 * @LastEditTime: 2023-03-23 17:06:04
 * @FilePath: /leetcode/template/math.go
 * @Description:数学
 */
package template

func FindIntersection(a []int, b []int) []int {
    lA, rA := a[0], a[1]

    lB, rB := b[0], b[1]

    // 比较两个区间的最大和最小值
    // 如果存在交集，则交集的最大值为两个最大值中的较小值
    // 交集的最小值为两个最小值中的较大值
    min := 0
    max := 0
    if rA < lB || rB < lA {
        // 两个区间没有交集
        return nil
    } else {
        // 两个区间有交集
        if rA < rB {
            max = rA
        } else {
            max = rB
        }
        if lA > lB {
            min = lA
        } else {
            min = lB
        }
    }
    return []int{min, max}
}

/**
 * @description: 返回所有整数的最小值
 * @param {int} first
 * @param {...int} others
 * @return {*} min 最小值
 */
func Min(first int, others ...int) int {
    min := first
    for _, v := range others {
        if v < min {
            min = v
        }
    }
    return min
}

/**
 * @description: 返回所有整数的最大值
 * @param {int} first
 * @param {...int} others
 * @return {*} max 最大值
 */
func Max(first int, others ...int) int {
    max := first
    for _, v := range others {
        if v >max {
            max = v
        }
    }
    return max
}

/**
 * @description: 返回最小值（空接口接受多类型参数）
 * @param {interface{}} first
 * @param {...interface{}} rest
 * @return {*} min
 */
func Minimum(first interface{}, rest ...interface{}) interface{} {
    min := first
    for _, v := range rest {
        switch v := v.(type) {
            case int:
                if v < min.(int) {
                    min = v
                }
            case float64:
                if v < min.(float64) {
                    min = v
                }
            case string:
                if v < min.(string) {
                    min = v
                }
            }
    }
    return min
}

/**
 * @description: 返回最小值（空接口接受多类型参数） 
 * @param {interface{}} first
 * @param {...interface{}} rest
 * @return {*} max
 */
func Maximum(first interface{}, rest ...interface{}) interface{} {
    max := first
    for _, v := range rest {
        switch v := v.(type) {
            case int:
                if v > max.(int) {
                    max = v
                }
            case float64:
                if v > max.(float64) {
                    max = v
                }
            case string:
                if v > max.(string) {
                    max = v
                }
            }
    }
    return max
}