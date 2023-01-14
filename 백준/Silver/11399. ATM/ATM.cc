#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> p(n);

	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}
	sort(p.begin(), p.end());

	int answer = 0;
	for (int i = 1; i < n; i++) {
		p[i] += p[i - 1];
		answer += p[i];
	}
	answer += p[0];
	cout << answer << endl;

	return 0;
}