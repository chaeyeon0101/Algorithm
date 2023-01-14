#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	vector<int> n_value(n);
	for (int i = 0; i < n; i++) {
		cin >> n_value[i];
	}

	int n_pick = n - 1;
	while (1) {
		if (n_value[n_pick] <= k) {
			break;
		}
		n_pick--;
	}

	int answer = 0;
	while (k > 0) {
		answer += k / n_value[n_pick];
		k %= n_value[n_pick];
		n_pick--;
	}

	cout << answer << endl;

	return 0;
}