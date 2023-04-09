/*
 * @Author: lmio
 * @Date: 2023-04-09 16:10:12
 * @LastEditTime: 2023-04-09 17:21:07
 * @FilePath: /leetcode/code/67.go
 * @Description:67. 二进制求和
 */
package code

import (
	"math/big"
)

func AddBinary(a string, b string) string {
	ai, _ := new(big.Int).SetString(a, 2)
	bi, _ := new(big.Int).SetString(b, 2)

	ai.Add(ai, bi)
	return ai.Text(2)
}