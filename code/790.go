/*
 * @Author: lmio
 * @Date: 2023-03-09 22:50:38
 * @LastEditTime: 2023-03-09 23:48:29
 * @FilePath: /leetcode/code/790.go
 * @Description:790.多米诺和托米诺平铺
 */
package code

func NumTilings(n int) int {
	var numTil func (int) int
	numTil = func(i int) int {
		if i < 0 {
			return 0
		}
        if i == 0 {
            return 1
        }
		if i < 3 {
			return i
		}
		
		return numTil(i-1) + numTil(i-2) + (2*numTil(i-3)) + (2*numTil(i-4))
	}
	return numTil(n) % 10000007
}