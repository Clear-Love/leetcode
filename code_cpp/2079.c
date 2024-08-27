int wateringPlants(int* plants, int plantsSize, int capacity) {
    int res = 0;
    int cap = capacity;
    for (int i = 0; i < plantsSize; i++) {
        res += 1;
        if (cap < plants[i]) {
            res += 2*i;
            cap = capacity;
        }
        cap -= plants[i];
    }
    return res;
}