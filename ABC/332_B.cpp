#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, G, M;
  cin >> N >> G >> M;
  int cup = 0;
  int glass = 0;

  for (int i = 0; i < N; i++)
  {
    if (glass == G)
    {
      glass = 0;
    }
    else if (cup == 0)
    {
      cup = M;
    }
    else
    {
      if (cup >= G - glass)
      {
        cup -= G - glass;
        glass = G;
      }
      else
      {
        glass += cup;
        cup = 0;
      }
    }
  }
  cout << glass << " " << cup << endl;
}