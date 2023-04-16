/*
 * @Author: lmio
 * @Date: 2023-04-16 12:02:31
 * @LastEditTime: 2023-04-16 13:34:48
 * @FilePath: /leetcode/offer/20.go
 * @Description:剑指 Offer 20. 表示数值的字符串
 */
package offer

type state int
type charType int

const (
    STATE_INITIAL state = iota
    STATE_INT_SIGN
    STATE_INTEGER
    STATE_POINT
    STATE_POINT_WITHOUT_INT
    STATE_DECIMAL
    STATE_EXP
    STATE_EXP_SIGN
    STATE_EXP_NUMBER
    STATE_END
)

const (
    CHAR_NUMBER charType = iota
    CHAR_EXP
    CHAR_POINT
    CHAR_SIGN
    CHAR_SPACE
    CHAR_ILLEGAL
)

func toCharType(ch byte) charType {
	switch ch {
	// 整数
    case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
        return CHAR_NUMBER
	// 指数标志
    case 'e', 'E':
        return CHAR_EXP
	// 小数点
    case '.':
        return CHAR_POINT
	// 符号位
    case '+', '-':
        return CHAR_SIGN
	// 空格
    case ' ':
        return CHAR_SPACE
	// 非法
    default:
        return CHAR_ILLEGAL
    }
}

var transformer = map[state]map[charType]state{
	STATE_INITIAL:{
		CHAR_SPACE: STATE_INITIAL,
		CHAR_SIGN: STATE_INT_SIGN,
		CHAR_POINT: STATE_POINT_WITHOUT_INT,
		CHAR_NUMBER: STATE_INTEGER,
	},
	STATE_INT_SIGN:{
		CHAR_NUMBER: STATE_INTEGER,
		CHAR_POINT: STATE_POINT_WITHOUT_INT,
	},
	STATE_INTEGER:{
		CHAR_NUMBER: STATE_INTEGER,
		CHAR_POINT: STATE_POINT,
		CHAR_EXP: STATE_EXP,
		CHAR_SPACE: STATE_END,
	},
	STATE_POINT:{
		CHAR_NUMBER: STATE_DECIMAL,
		CHAR_EXP: STATE_EXP,
		CHAR_SPACE: STATE_END,
	},
	STATE_POINT_WITHOUT_INT:{
		CHAR_NUMBER: STATE_DECIMAL,
	},
	STATE_DECIMAL:{
		CHAR_NUMBER: STATE_DECIMAL,
		CHAR_EXP: STATE_EXP,
		CHAR_SPACE: STATE_END,
	},
	STATE_EXP:{
		CHAR_NUMBER: STATE_EXP_NUMBER,
		CHAR_SIGN: STATE_EXP_SIGN,
	},
	STATE_EXP_SIGN:{
		CHAR_NUMBER: STATE_EXP_NUMBER,
	},
	STATE_EXP_NUMBER:{
		CHAR_NUMBER: STATE_EXP_NUMBER,
		CHAR_SPACE: STATE_END,
	},
	STATE_END:{
		CHAR_SPACE: STATE_END,
	},
}

func IsNumber(s string) bool {
	state := STATE_INITIAL
	for i := range s {
		sta, ok := transformer[state][toCharType(s[i])]
		if !ok {
			// 非法输入
			return false
		}
		state = sta
	}
	return state == STATE_DECIMAL ||
			state == STATE_EXP_NUMBER ||
			state == STATE_INTEGER ||
			state == STATE_END ||
			state == STATE_POINT
}