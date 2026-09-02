#include <bits/stdc++.h>
using namespace std;

int main() {
	// read in the input, store the algorithms in a vector, algorithms
	int N, x;
	cin >> N >> x;
	vector<int> algorithms(N);
	for (int &t : algorithms) { cin >> t; }
	sort(algorithms.begin(), algorithms.end());
	int count = 0;  // number of minutes used so far
	int i = 0;
	while (i < N && count + algorithms[i] <= x) {
		// while there is enough time, learn more algorithms
		count += algorithms[i];
		i++;
	}
	cout << i << endl;  // print the ans
}