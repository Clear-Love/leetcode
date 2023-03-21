/*
 * @Author: lmio
 * @Date: 2023-02-12 21:32:17
 * @LastEditTime: 2023-02-19 23:26:25
 * @FilePath: /leetcode/code/22.go
 * @Description:22.括号生成
 */
package code

func GenerateParenthesis(n int) []string {
	var backtrace func(int, int)
	ans := []string{}
	res := ""

	/**
	* @description: 回溯算法，其实就是每对括号匹配数量的不同排列
	* @param {int} k 括号层数
	* @param {int} bracket 未匹配括号数
	* @return {*}
	*/
	backtrace = func(k int, bracket int) {
		if k == n {
			temp := res
			temp += "("
			for i := 0; i <= bracket; i++ {
				temp += ")"
			}
			ans = append(ans, temp)
			return
		}
		temp := res
		res += "("
		bracket++ 
		backtrace(k+1, bracket)
		
		for bracket > 0 {
			res += ")"
			bracket--
			backtrace(k+1, bracket)
		}
		res = temp
	}
	backtrace(1, 0)
	return ans
}