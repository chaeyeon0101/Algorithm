#include <iostream>
using namespace std;

int n, s;
int arr[20];
int cnt = 0;

void backtracking(int num, int start, int level, int result) {
	if (num == level) {
		if (result == s) {
			cnt++;
		}
		return;
	}

	for (int i = start; i < n; i++) {
		int sum = result;
		sum += arr[i];
		backtracking(num, i + 1, level + 1, sum);
	}
}

void subset_num() {
	for (int i = 1; i <= n; i++) {
		backtracking(i, 0, 0, 0);
	}
}

int main() {
	cin >> n >> s;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	subset_num();

	cout << cnt;
}