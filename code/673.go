/*
 * @Author: lmio
 * @Date: 2023-04-06 15:41:56
 * @LastEditTime: 2023-04-06 17:31:00
 * @FilePath: /leetcode/code/673.go
 * @Description:673. 最长递增子序列的个数
 */
package code

func FindNumberOfLIS(nums []int) int {
	type Cnt struct {
		Val int
		Count int
	}
	// tails表示长度为i的递增子序列的尾数
	tails := make([][]*Cnt, len(nums)+1)
	for i := 0; i < len(tails); i++ {
		tails[i] = []*Cnt{}
	}
	length := 1
	for _, num := range nums {
		l, r := 1, length
		// 找到大于num的第一个值
		for l < r {
			mid := (l + r) / 2
			if num > tails[mid][len(tails[mid])-1].Val {
				l = mid + 1
			}else {
				r = mid
			}
		}
		cur := &Cnt{Val: num}
		tails[l] = append(tails[l], cur)
		if l == 1 {
			cur.Count = 1
		}
		for i := 0; i < len(tails[l-1]); i++ {
			if tails[l-1][i].Val < num {
				cur.Count += tails[l-1][i].Count
			}
		}
		if length == l {
			length++
		}
	}
	res := 0
	for _, val := range tails[length-1] {
		res += val.Count
	}
	return res
}