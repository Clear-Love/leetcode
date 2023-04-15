/*
 * @Author: lmio
 * @Date: 2023-04-15 15:48:17
 * @LastEditTime: 2023-04-15 16:12:20
 * @FilePath: /leetcode/offer/31.go
 * @Description:剑指 Offer 31. 栈的压入、弹出序列
 */
package offer

func ValidateStackSequences(pushed, popped []int) bool {
	popPtr := 0
	stack := make([]int, 0, len(pushed))
	for i := 0; i < len(pushed); i++ {
		stack = append(stack, pushed[i])
		for stack[len(stack)-1] == popped[popPtr] {
			popPtr++
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}