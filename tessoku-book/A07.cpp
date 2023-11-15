#include <bits/stdc++.h>
using namespace std;

int D, N, days[300000];

int main() {
  cin >> D >> N;
  for(int i=1; i<=N; i++) {
    int L,R;
    cin >> L >> R;
    for(int j=L; j<R+1; j++) days[j]++;
  }
  
  for(int i=1; i<=D; i++) cout << days[i] << endl;
}