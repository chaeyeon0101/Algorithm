#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<int> num;
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		num.push_back(tmp);
	}

	int answer = -100000;
	int i = 0;
	while (i < n) {
		if (num[i] >= 0) {
			break;
		}
		if (answer < num[i]) {
			answer = num[i];
		}
		i++;
	}
	if (i == n) {
		cout << answer << endl;
		return 0;
	}

	int sum = 0;
	for (; i < n; i++) {
		int m = 0;
		while (i < n && num[i] < 0) {
			m += num[i];
			i++;
		}
		sum += m;
		if (sum < 0) {
			sum = 0;
			i--;
			continue;
		}

		while (i < n && num[i] >= 0) {
			sum += num[i];
			i++;
		}
		if (sum > answer) {
			answer = sum;
		}
		i--;
	}

	cout << answer << endl;
	return 0;
}