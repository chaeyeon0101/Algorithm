#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<pair<int, int>> Meeting_Schedule;
	int answer = 0;
	for (int i = 0; i < n; i++) {
		int start_time;
		int end_time;
		cin >> start_time >> end_time;
		Meeting_Schedule.push_back(make_pair(end_time, start_time));
	}
	sort(Meeting_Schedule.begin(), Meeting_Schedule.end());

	int time = Meeting_Schedule[0].first;
	++answer;
	for (int i = 1; i < n; i++) {
		if (time <= Meeting_Schedule[i].second) {
		    time = Meeting_Schedule[i].first;
		    answer++;
        }
	}
	cout << answer << endl;

	return 0;
}