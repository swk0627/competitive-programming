#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n, a, cnt = 0;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> a;
        for(int j=2; j*j<=a; j++) {
            if(a%j==0) {
                cnt++;
                break;
            }
        }
    }
    cout << n - cnt << endl;
}