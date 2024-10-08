/*
 * @Author: lmio
 * @Date: 2023-02-19 23:30:39
 * @LastEditTime: 2023-08-05 01:17:09
 * @FilePath: /leetcode/utils/math.go
 * @Description:数学
 */
package utils

import "math/big"

type Ordered interface {
	Integer | Float | ~string
}

type Integer interface {
	Signed | Unsigned
}

type Signed interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

type Unsigned interface {
	~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

type Float interface {
	~float32 | ~float64
}

/**
 * @description: 返回两个区间的交集
 * @param {[]int} a A区间
 * @param {[]int} b B区间
 * @return {*}
 */
func FindIntersection[T Integer](a []T, b []T) []T {
	lA, rA := a[0], a[1]

	lB, rB := b[0], b[1]

	// 比较两个区间的最大和最小值
	// 如果存在交集，则交集的最大值为两个最大值中的较小值
	// 交集的最小值为两个最小值中的较大值
	var min T = 0
	var max T = 0
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
	return []T{min, max}
}

/**
 * @description: 返回所有整数的最小值
 * @param {int} first
 * @param {...int} others
 * @return {*} min 最小值
 */
func Min[T Ordered](first T, others ...T) T {
	min := first
	for _, v := range others {
		if v < min {
			min = v
		}
	}
	return min
}

/**
 * @description: 返回切片的最小值
 * @return {*}
 */
func MinSlice[T Ordered](slice []T) T {
	if len(slice) == 0 {
		panic("cant ont empty slice")
	}
	min := slice[0]
	for _, v := range slice {
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
func Max[T Ordered](first T, others ...T) T {
	max := first
	for _, v := range others {
		if v > max {
			max = v
		}
	}
	return max
}

/**
 * @description: 返回切片的最小值
 * @return {*}
 */
func MaxSlice[T Ordered](slice []T) T {
	if len(slice) == 0 {
		panic("cant ont empty slice")
	}
	max := slice[0]
	for _, v := range slice {
		if v > max {
			max = v
		}
	}
	return max
}

/**
 * @description: 求绝对值
 * @return {*}
 */
func Abs[T Signed](v T) T {
	if v < 0 {
		return -v
	}
	return v
}

/**
 * @description: 计算阶层
 * @param {int} n
 * @return {*}
 */
func Factorial(n int64) *big.Int {
	if n == 0 {
		return big.NewInt(1)
	}
	if n < 0 {
		return big.NewInt(-1)
	}
	out := big.NewInt(1)
	out.MulRange(1, n)
	return out
}

/**
 * @description: 计算排列数
 * @param {*} n 总数
 * @param {int} k 选取的数目
 * @return {*}
 */
func PermutationCount(n, m int64) *big.Int {
	out := big.NewInt(0)
	n1 := Factorial(n)
	n2 := Factorial(n - m)
	return out.Div(n1, n2)
}

/**
 * @description: 计算组合数 :( 其实big.Int有api Binomial)
 * @param {*} n 总数
 * @param {int} k 选取的数目
 * @return {*}
 */
func CombinationsCount(n, m int64) *big.Int {
	out := big.NewInt(0)
	n1 := Factorial(n)
	m1 := Factorial(m)
	n2 := Factorial(n - m)
	out1 := big.NewInt(0)
	return out.Div(n1, out1.Mul(m1, n2))
}

/**
 * @description: 求整数最高位
 * @param {int} n
 * @return {*}
 */
func GetHighestDigit(n int) int {
	for n > 9 {
		n /= 10
	}
	return n
}

/**
 * @description: 求两个数的最大公约数(使用辗转相除法)
 * @param {*} a
 * @param {int} b
 * @return {*}
 */
func Gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return Gcd(b, a%b)
}

/**
 * @description: 循环求余，正确计算x^a对p求余的值
 * @param {*} x
 * @param {*} a
 * @param {int} p
 * @return {*}
 */
func Remainder(x, a, p int) int {
	res := 1
	for i := 0; i < a; i++ {
		res = (res * x) % p
	}
	return res
}