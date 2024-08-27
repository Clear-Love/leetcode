/*
 * @Author: lmio 2091319361@qq.com
 * @Date: 2024-08-22 14:22:33
 * @LastEditors: lmio 2091319361@qq.com
 * @Description:146. LRU 缓存
 */
#include <bits/stdc++.h>

using namespace std;

template <typename K, typename V> class LRUCache {
    using Node = pair<K, V>;
    list<Node> cache;
    unordered_map<int, typename list<Node>::iterator> cache_map;
    int capacity;

public:
    LRUCache(int capacity) : capacity(capacity) {
    }

    int get(K key) {
        auto it = cache_map.find(key);
        if (it == cache_map.end()) {
            return -1;
        }
        // 将 key 移动到头部
        auto val = *it->second;
        cache.erase(it->second);
        cache.push_front(val);
        cache_map[key] = cache.begin();
        return val.second;
    }

    void put(K key, V value) {
        // key 存在，修改 key 的值，并将 key 移动到头部
        auto it = cache_map.find(key);
        if (it != cache_map.end()) {
            cache.erase(it->second);
            cache.emplace_front(key, move(value));
            cache_map[key] = cache.begin();
            return;
        }
        // key 不存在，添加 key 到头部
        if (cache.size() == capacity) {
            // 容量不够，删除尾部元素
            auto last = cache.back();
            cache.pop_back();
            cache_map.erase(last.first);
        }
        cache.emplace_front(key, move(value));
        cache_map[key] = cache.begin();
        return;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */