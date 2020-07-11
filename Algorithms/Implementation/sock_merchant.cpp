#include <bits/stdc++.h>

using namespace std;

int sockMerchant(int n, vector <int> ar) {
    // Complete this function
    vector<int> count(100);
    for (int i=0; i<100; i++){
        count[i] = 0;
    }
    int total_pair = 0;
    for (int i=0; i<n; i++){
        if (count[ar[i]-1]==1)
        {
            total_pair += 1;
            count[ar[i]-1] = 0;
        }
        else
            count[ar[i]-1]=1;
    }
    return total_pair;
    
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = sockMerchant(n, ar);
    cout << result << endl;
    return 0;
}