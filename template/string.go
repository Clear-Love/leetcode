/*
 * @Author: lmio
 * @Date: 2023-02-25 14:12:24
 * @LastEditTime: 2023-04-02 00:19:32
 * @FilePath: /leetcode/template/string.go
 * @Description:字符串处理
 */
package template

import "unsafe"


/**
 * @description: byte切片转字符串
 * @param {[]byte} bs
 * @return {*}
 */
func ToString(bs []byte)string{
    //return *(*string)(unsafe.Pointer(&bs))
    return unsafe.String(unsafe.SliceData(bs), len(bs))
}

/**
 * @description: 字符串装byte切片
 * @param {string} s
 * @return {*}
 */
func ToBytes(s string) []byte {
    // x := (*[2]uintptr)(unsafe.Pointer(&s))
    // h := [3]uintptr{x[0], x[1], x[1]}
    // return *(*[]byte)(unsafe.Pointer(&h))
    return unsafe.Slice(unsafe.StringData(s), len(s))
}