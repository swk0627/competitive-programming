#include <iostream>
#include <limits.h>
using namespace std;
int main() {
    int n, r;
    int min = INT_MAX, max = INT_MIN;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> r;
        if(max < r - min) max = r - min;
        if(min > r) min = r;
    }
    cout << max << endl;
}