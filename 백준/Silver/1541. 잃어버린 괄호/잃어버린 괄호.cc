#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	cin >> s;

	bool code = false;

	string s_tmp;
	int i_tmp = 0;
	int answer = 0;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+') {
			//cout << "+ enter" << endl;
			i_tmp += stoi(s_tmp);
			//cout << "i_tmp = " << i_tmp << endl;
			string tmp;
			s_tmp = tmp;
			continue;
		}
		else if (s[i] == '-') {
			//cout << "- enter" << endl;
			i_tmp += stoi(s_tmp);
			//cout << "i_tmp = " << i_tmp << endl;
			if (code) {
				answer -= i_tmp;
			}
			else {
				answer += i_tmp;
				code = true;
			}
			//cout << "answer = " << answer << endl;
			string tmp;
			s_tmp = tmp;
			i_tmp = 0;
			continue;
		}
		s_tmp += s[i];
		//cout << i << "번째 " << s_tmp << endl;
	}
	//cout << "last enter" << endl;
	i_tmp += stoi(s_tmp);
	//cout << "i_tmp = " << i_tmp << endl;
	if (code) {
		answer -= i_tmp;
	}
	else {
		answer += i_tmp;
		code = true;
	}

	cout << answer << endl;

	return 0;
}