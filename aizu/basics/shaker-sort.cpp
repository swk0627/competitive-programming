#include <iostream>
using namespace std;
int main() {
    int n, i, j, tmp;
    cin >> n;
    int a[n];
    for(i=0; i<n; i++) {
        cin >> a[i];
    }
    for(int cnt=0; cnt<n; cnt++) {
            cout << a[cnt] << " ";
            if(cnt==n-1) cout << endl;
    }
    for(i=0; i<n-1; i++) {
        bool flag = true;
        for(j=0; j<n-1; j++) {
            if(a[j] > a[j+1]) {
                tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                flag = false;
            }
        }
        for(j=n-1; j>0; j--) {
            if(a[j] < a[j-1]) {
                tmp = a[j];
                a[j] = a[j-1];
                a[j-1] = tmp;
                flag = false;
            }
        }
        if(flag) exit(1);
        for(int cnt=0; cnt<n; cnt++) {
            cout << a[cnt] << " ";
            if(cnt==n-1) cout << endl;
        }
    }
}