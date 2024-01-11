#include <iostream>
using namespace std;

int main()
{

    int n;
    cin >> n;
    int ans = 0;
    while (n != 0)
    {
        int ld = n % 10;
        ans = ans * 10 + ld;
        n = n / 10;
    }
    cout << ans << endl;
}