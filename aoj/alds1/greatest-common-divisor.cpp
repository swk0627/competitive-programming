#include <iostream>
using namespace std;
int main() {
    int a, b;
    int tmp;
    int r;
    cin >> a >> b;
    if(a < b) {
        tmp = a;
        a = b;
        b = tmp;
    }
    while(a % b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    cout << b << endl;
}