/*
 * @Author: lmio
 * @Date: 2023-02-03 01:52:08
 * @LastEditTime: 2023-02-19 23:28:41
 * @FilePath: /leetcode/code/278.go
 * @Description:278.第一个错误的版本
 */

package code

func FirstBadVersion(n int) int{
	left, right := 1, n
	for left < right {
		mid := (left + right) >> 1
		if isBadVersion(mid){
			right = mid
		}else {
			left = mid + 1
		}
	}
	return left
}

func isBadVersion(version int) bool{
  	return version == 1		
}