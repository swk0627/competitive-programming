#include <iostream>
using namespace std;
int main() {
    int n, tmp;
    int max_num = 0;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> tmp;
        if(max_num < tmp) max_num = tmp;
    }
    cout << max_num << endl;
}