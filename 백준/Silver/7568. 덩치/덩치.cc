#include <bits/stdc++.h>
using namespace std;

int people[50][3] = { 0 };

void bruteforcing(int n) {
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == j) continue;
			if (people[i][0] < people[j][0] && people[i][1] < people[j][1]) {
				people[i][2]++;
			}
		}
	}

	return;
}

int main(void) {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> people[i][0] >> people[i][1];
	}

	bruteforcing(n);

	for (int i = 0; i < n; i++) {
		cout << people[i][2] + 1 << " ";
	}

	return 0;
}