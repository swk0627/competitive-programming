#include <iostream>
using namespace std;
int main() {
    int n, i;
    cin >> n;
    int a[n];
    for(i=0; i<n; i++) {
        cin >> a[i];
    }
    for(i=0; i<n; i++) {
        int idx = i;
        int num = a[i];
        for(int j=i-1; j>=0; j--){
            if(i==0) break;
            if(num < a[j]) {
                a[j+1] = a[j];
                idx = j;
            }
        }
        a[idx] = num;
        for(int cnt=0; cnt<n; cnt++) {
            cout << a[cnt];
            if(cnt==n-1) cout << endl;
            else cout << " ";
        }
    }
}