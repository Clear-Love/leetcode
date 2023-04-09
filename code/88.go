/*
 * @Author: lmio
 * @Date: 2023-04-09 18:25:02
 * @LastEditTime: 2023-04-09 18:55:50
 * @FilePath: /leetcode/code/88.go
 * @Description:88. 合并两个有序数组
 */
package code

func Merge(nums1 []int, m int, nums2 []int, n int) {
	p1, p2 := m-1, n-1
	i := n+m-1
	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] > nums2[p2] {
			nums1[i] = nums1[p1]
			p1--
		}else {
			nums1[i] = nums2[p2]
			p2--
		}
		i--
	}
	if p1 < 0 {
		for p2 >= 0 {
			nums1[i] = nums2[p2]
			p2--
			i--
		}
	}else {
		for p1 >= 0 {
			nums1[i] = nums1[p1]
			p1--
			i--
		}
	}
}