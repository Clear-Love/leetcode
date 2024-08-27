/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-10 10:36:28
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 65. 有效数字
 */
#include <stdbool.h>

enum STATE {
    STATE_START, // 初始状态
    STATE_SIGN, // 符号状态
    STATE_NUMBER, // 数字状态
    STATE_POINT, // 小数点状态
    STATE_POINT_WITHOUTNUMBER, // 没有数字的小数点状态
    STATE_FRACTION, // 小数状态
    STATE_EXP, // 指数状态（e/E）
    STATE_EXP_SIGN, // 指数符号状态
    STATE_EXP_NUMBER, // 指数数字状态
};

enum CharType {
    CHAR_NUMBER, // 数字
    CHAR_EXP, // 指数符号(e/E)
    CHAR_POINT, // 小数点
    CHAR_SIGN, // 符号 (-/+)
    CHAR_INVALID, // 无效字符
    CHAR_END, // 结束符(\0)
};

enum CharType toCharType(char ch) {
    if (ch >= '0' && ch <= '9') {
        return CHAR_NUMBER;
    } else if (ch == 'e' || ch == 'E') {
        return CHAR_EXP;
    } else if (ch == '.') {
        return CHAR_POINT;
    } else if (ch == '+' || ch == '-') {
        return CHAR_SIGN;
    } else if (ch == '\0') {
        return CHAR_END;
    } else {
        return CHAR_INVALID;
    }
}

bool isNumber(char* s) {
    enum STATE state = STATE_START;
    while (1) {
        enum CharType type = toCharType(*s);
        if (type == CHAR_INVALID) {
            return false;
        }
        switch (state) {
            case STATE_START:
                switch (type) {
                    case CHAR_SIGN:
                        state = STATE_SIGN;
                        break;
                    case CHAR_NUMBER:
                        state = STATE_NUMBER;
                        break;
                    case CHAR_POINT:
                        state = STATE_POINT_WITHOUTNUMBER;
                        break;
                    default:
                        return false;
                }
                break;
            case STATE_SIGN:
                switch (type) {
                    case CHAR_NUMBER:
                        state = STATE_NUMBER;
                        break;
                    case CHAR_POINT:
                        state = STATE_POINT_WITHOUTNUMBER;
                        break;
                    default:
                        return false;
                }
                break;

            case STATE_NUMBER:
                switch (type) {
                    case CHAR_NUMBER:
                        break;
                    case CHAR_POINT:
                        state = STATE_POINT;
                        break;
                    case CHAR_EXP:
                        state = STATE_EXP;
                        break;
                    case CHAR_END: // 有效整数
                        return true;
                    default:
                        return false;
                }
                break;
            case STATE_POINT:
                switch (type) {
                    case CHAR_NUMBER:
                        state = STATE_FRACTION;
                        break;
                    case CHAR_EXP:
                        state = STATE_EXP;
                        break;
                    case CHAR_END: // 有效整数
                        return true;
                    default:
                        return false;
                }
                break;
            case STATE_POINT_WITHOUTNUMBER:
                switch (type) {
                    case CHAR_NUMBER:
                        state = STATE_FRACTION;
                        break;
                    default:
                        return false;
                }
            case STATE_FRACTION:
                switch (type) {
                    case CHAR_NUMBER:
                        break;
                    case CHAR_EXP:
                        state = STATE_EXP;
                        break;
                    case CHAR_END: // 有效小数
                        return true;
                    default:
                        return false;
                }
                break;
            case STATE_EXP:
                switch (type) {
                    case CHAR_SIGN: // 指数符号位
                        state = STATE_EXP_SIGN;
                        break;
                    case CHAR_NUMBER:
                        state = STATE_EXP_NUMBER;
                        break;
                    default:
                        return false;
                }
                break;
            case STATE_EXP_SIGN:
                switch (type) {
                    case CHAR_NUMBER:
                        state = STATE_EXP_NUMBER;
                        break;
                    default:
                        return false;
                }
                break;
            case STATE_EXP_NUMBER:
                switch (type) {
                    case CHAR_NUMBER:
                        break;
                    case CHAR_END: // 有效指数
                        return true;
                    default:
                        return false;
                }
        }
        s++;
    }
}