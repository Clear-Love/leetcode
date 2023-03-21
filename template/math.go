/*
 * @Author: lmio
 * @Date: 2023-02-19 23:30:39
 * @LastEditTime: 2023-02-21 20:16:43
 * @FilePath: /leetcode/template/math.go
 * @Description:数学
 */
package template


func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

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
