/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-08 16:46:55
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 1491. 去掉最低工资和最高工资后的工资平均值
 */
#include <limits.h>
#include <stdio.h>
#include <math.h>

double average(int* salary, int salarySize) {
    if (salarySize < 2) return 0.0;
    int max = INT_MIN, min = INT_MAX, sum = 0;
    for (int i = 0; i < salarySize; i++) {
        if (max < salary[i]) max = salary[i];
        if (min > salary[i]) min = salary[i];
        sum += salary[i];
    }
    return (double)(sum - max - min) / (salarySize - 2);
}