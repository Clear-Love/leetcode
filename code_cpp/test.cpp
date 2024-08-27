#include <bits/stdc++.h>

using namespace std;

extern "C" {
struct BDL {
    char t : 4;
    char k : 4;
    unsigned short i : 8;
    unsigned long m;
};
}

int main() {
    cout << sizeof(struct BDL) << endl;
    return 0;
}