#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n, tmp;
    int min, minj, cnt=0;
    cin >> n;
    short a[n];
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }
    for(int i=0; i<n-1; i++) {
        min = a[i];
        minj = i;
        for(int j=i+1; j<n; j++) {
            if(min > a[j]) {
                min = a[j];
                minj = j;
            }
        }
        if(a[i] != a[minj]) cnt++;
        tmp = a[i];
        a[i] = a[minj];
        a[minj] = tmp;
    }
    for(int i=0; i<n; i++) {
        cout << a[i];
        if(i==n-1) cout << endl;
        else cout << " ";
    }
    cout << cnt << endl;
}