/*
 * @Author: lmio
 * @Date: 2023-04-05 19:23:23
 * @LastEditTime: 2023-04-05 20:50:46
 * @FilePath: /leetcode/code/139.go
 * @Description:139. 单词拆分
 */
package code

func WordBreak(s string, wordDict []string) bool {
	Dict := make(map[string]bool)
    for _, w := range wordDict {
        Dict[w] = true
    }
    dp := make([]bool, len(s) + 1)
    dp[0] = true
    for i := 1; i <= len(s); i++ {
        for j := 0; j < i; j++ {
            if dp[j] && Dict[s[j:i]] {
                dp[i] = true
                break
            }
        }
    }
    return dp[len(s)]
}