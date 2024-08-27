/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-09 18:53:05
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2105. 给植物浇水 II
 */
#include<stdio.h>

int minimumRefill(int* plants, int plantsSize, int capacityA, int capacityB) {
    int left = 0, right = plantsSize-1;
    int waterA = capacityA, waterB = capacityB;
    int res = 0;
    while (left <= right){
        if (left == right) {
            if (waterA < plants[left] && waterB < plants[left]) {
                return res+1;
            }
            return res;
        }
        if (plants[left] > waterA) {
            waterA = capacityA;
            res++;
        }
        if (plants[right] > waterB) {
            waterB = capacityB;
            res++;
        }
        waterA -= plants[left++];
        waterB -= plants[right--];
    }
    return res;
}

int main(int argc, char const *argv[]) {
    int plants[] = {1,2,4,4,5};
    int res = minimumRefill(plants, 5, 6, 5);
    printf("%d", res);
    return 0;
}
