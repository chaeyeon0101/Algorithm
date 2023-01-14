#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> graph(1001);
bool visited[1001] = { false };

void dfs(int start) {
	visited[start] = true;
	cout << start << ' ';

	for (int i = 0; i < graph[start].size(); i++) {
		if (!visited[graph[start][i]]) {
			dfs(graph[start][i]);
		}
	}
	return;
}

void bfs(int start) {
	queue<int> q;
	q.push(start);
	visited[start] = true;
	cout << start << ' ';

	while (!q.empty()) {
		int n = q.front();
		q.pop();

		for (int i = 0; i < graph[n].size(); i++) {
			if (!visited[graph[n][i]]) {
				q.push(graph[n][i]);
				visited[graph[n][i]] = true;
				cout << graph[n][i] << ' ';
			}
		}
	}
	cout << endl;
	return;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cout.tie(NULL); 
    cin.tie(NULL);
    
	int n, m, v;
	cin >> n >> m >> v;
	
	for (int i = 0; i < m; i++) {
		int tmp_a, tmp_b;
		cin >> tmp_a >> tmp_b;
		graph[tmp_a].push_back(tmp_b);
		graph[tmp_b].push_back(tmp_a);
	}
	for (int i = 1; i <= n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	dfs(v);
	cout << endl;
	memset(visited, false, (n + 1) * sizeof(bool));
	bfs(v);

	return 0;
}