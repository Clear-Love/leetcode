/*
 * @Author: lmio
 * @Date: 2023-04-18 15:51:29
 * @LastEditTime: 2023-04-19 15:28:57
 * @FilePath: /leetcode/offer/59-I.go
 * @Description:剑指 Offer 59 - I. 滑动窗口的最大值
 */
package offer

func MaxSlidingWindow(nums []int, k int) []int {
    q := make([]int, 0, k)
    push := func(index int) {
        // 单调栈，如果在滑动窗口内，下标小的数小于下标大的数
        // 那么在滑动窗口向右移动的过程中，下标较小的数将永远不会数滑动窗口的最大值，基于这一性质
        // 可以把所有添加元素左侧元素永久移除
        i := len(q)-1
        for i >= 0 && nums[q[i]] < nums[index]{
            q = q[:i]
            i--
        }
        q = append(q, index)
        if index - q[0] >= k {
            q = q[1:]
        }
    }
    n := len(nums)
    res := make([]int, 0, n-k+1)
    for i := 0; i < k; i++ {
        push(i)
    }
    res = append(res, nums[q[0]])
    for i := k; i < n; i++ {
        push(i)
        res = append(res, nums[q[0]])
    }
    return res
}