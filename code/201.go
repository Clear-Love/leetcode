/*
 * @Author: lmio
 * @Date: 2023-04-09 13:34:45
 * @LastEditTime: 2023-04-09 14:02:17
 * @FilePath: /leetcode/code/201.go
 * @Description:201. 数字范围按位与
 */
package code

func RangeBitwiseAnd(left, right int) int {
	for left < right {
		// 把末尾的1变为0
        right &= (right - 1)
    }
    return right
}