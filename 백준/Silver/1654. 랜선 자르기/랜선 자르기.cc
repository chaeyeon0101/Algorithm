#include <bits/stdc++.h>
using namespace std;

int main() {
	// 입력을 받음.
	int k, n;
	cin >> k >> n;
	vector <long long> len;
	for (int i = 0; i < k; i++) {
		long long tmp;
		cin >> tmp;
		len.push_back(tmp);
	}
	sort(len.rbegin(), len.rend());

	// check(start)!=check(end)(start는 T, end는 F)를 만들기 위해 end가 T인 경우를 확인해줌.
	long long start = 0;
	long long end = len[0];
	for (int i = 0; i < len.size(); i++) {
		start += len[i] / end;
	}
	if (start >= n) {
		cout << end << endl;
		return 0;
	}

	start = 1;
	while (start + 1 < end) {
		int cnt = 0;
		long long mid = (start + end) / 2;
		for (int i = 0; i < len.size(); i++) {
			cnt += len[i] / mid;
		}
		if (cnt >= n) start = mid;
		else end = mid;
	}
	cout << start << endl;

	return 0;
}