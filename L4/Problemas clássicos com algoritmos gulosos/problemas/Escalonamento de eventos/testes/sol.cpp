#include <bits/stdc++.h>
using namespace std;
#define MAXN 200100
typedef pair<int, int> pii;
#define F first
#define S second
pii movie[MAXN];
int n;
 
bool ordena(pii a, pii b){
  return a.S < b.S;
}
 
int main (){
  cin.tie(0); cin.sync_with_stdio(0);
  
  cin >> n;
  for(int i = 0; i < n; i++){
    int a, b;
    cin >> a >> b;
    movie[i] = {a,b};
  }
  
  sort(movie, movie+n, ordena);
  
  int f = -1;
  int r = 0;
  for(int i = 0; i < n; i++){
    if(movie[i].F >= f){
      f = movie[i].S;
      r++;
    }
  }
  
  cout << r << endl;
}