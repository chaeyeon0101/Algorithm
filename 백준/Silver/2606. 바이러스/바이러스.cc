#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> network(101);
bool visited[101] = { false };

int dfs() {
	int answer = 0;

	stack<int> s;
	s.push(1);
	visited[1] = true;

	while (!s.empty()) {
		int n = s.top();
		s.pop();

		for (int i = 0; i < network[n].size(); i++) {
			if (!visited[network[n][i]]) {
				s.push(network[n][i]);
				visited[network[n][i]] = true;
				answer++;
			}
		}
	}
	return answer;
}

int main(void) {
	int com_num, connect_net;
	cin >> com_num >> connect_net;

	for (int i = 0; i < connect_net; i++) {
		int tmp_a, tmp_b;
		cin >> tmp_a >> tmp_b;
		network[tmp_a].push_back(tmp_b);
		network[tmp_b].push_back(tmp_a);
	}

	cout << dfs();
}