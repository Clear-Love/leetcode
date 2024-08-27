/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-05-10 09:53:53
 * @LastEditors: lmio 2091319361@qq.com
 * @Description: 2960. 统计已测试设备
 */

int countTestedDevices(int* batteryPercentages, int batteryPercentagesSize) {
    int res = 0;
    for(int i = 0; i < batteryPercentagesSize; i++){
        if (batteryPercentages[i] > res) {
            res++;
        }
    }
    return res;
}