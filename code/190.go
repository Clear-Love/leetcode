/*
 * @Author: lmio
 * @Date: 2023-02-13 16:28:53
 * @LastEditTime: 2023-02-19 23:28:03
 * @FilePath: /leetcode/code/190.go
 * @Description:190.颠倒二进制位
 */
package code

const (
    m1 = 0x55555555 // 01010101010101010101010101010101
    m2 = 0x33333333 // 00110011001100110011001100110011
    m4 = 0x0f0f0f0f // 00001111000011110000111100001111
    m8 = 0x00ff00ff // 00000000111111110000000011111111
)


/**
 * @description: 递归反转二进制数，类似于归并排序
 * @param {uint32} n
 * @return {*}
 */
func ReverseBits(n uint32) uint32 {
	// 奇数位和偶数位互换
    n = n>>1&m1 | n&m1<<1
    n = n>>2&m2 | n&m2<<2
    n = n>>4&m4 | n&m4<<4
    n = n>>8&m8 | n&m8<<8
    return n>>16 | n<<16
}