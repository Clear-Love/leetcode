/*
 * @Author: lmio
 * @Date: 2023-02-25 14:12:24
 * @LastEditTime: 2023-02-25 14:12:26
 * @FilePath: /leetcode/template/string.go
 * @Description:字符串处理
 */
package template

import "unsafe"

func ToString(bs[]byte)string{ 
   return*(*string)(unsafe.Pointer(&bs)) 
}