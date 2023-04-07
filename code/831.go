/*
 * @Author: lmio
 * @Date: 2023-04-01 22:54:22
 * @LastEditTime: 2023-04-02 00:17:29
 * @FilePath: /leetcode/code/831.go
 * @Description:831.隐藏个人信息
 */
package code

import (
	"leetcode/utils"
	"strings"
	"unicode"
)

func MaskPII(s string) string {
    at := strings.Index(s, "@")
    if at > 0 {
        s = strings.ToLower(s)
        return strings.ToLower(string(s[0])) + "*****" + s[at-1:]
    }
    bs := make([]byte, 0, len(s))
    for i := 0; i < len(s); i++ {
        ch := s[i]
        if unicode.IsDigit(rune(ch)) {
            bs = append(bs, ch)
        }
    }
    s = utils.ToString(bs)
    country := []string{"", "+*-", "+**-", "+***-"}
    return country[len(s)-10] + "***-***-" + s[len(s)-4:]
}