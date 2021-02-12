#include <iostream>
using namespace std;
int main() {
    int n, i, j, tmp;
    cin >> n;
    int a[n];
    int cnt = 0;
    for(i=0; i<n; i++) {
        cin >> a[i];
    }
    for(i=0; i<n-1; i++) {
        bool flag = true;
        for(j=0; j<n-1; j++) {
            if(a[j] > a[j+1]) {
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                flag = false;
                cnt++;
            }
        }
        if(flag) break;
    }
    for(i=0; i<n; i++) {
        cout << a[i];
        if(i==n-1) cout << endl;
        else cout << " ";
    }
    cout << cnt << endl;
}