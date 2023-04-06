// 判断栈的输入输出是否合法
#include<iostream>
#include<stack>
using namespace std;

bool islegal(int *in, int *out, int n) {
	stack<int> s;
	s.push(in[0]);
	int p1 = 1;
	int p2 = 0;
	while (p2 < n) {
		while (p1 < n && out[p2] != s.top()) {
			s.push(in[p1]);
			p1 += 1;
		}
		if (p2 < n  && out[p2] != s.top()) {
			return false;
		}
		s.pop();
		p2++;
	}
	return true;
}

int main() {
	int T, n;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n;
		int in[100];
		int out[100];
		for (int j = 0; j < n; j++) {
			cin >> in[j];
		}
		for (int j = 0; j < n; j++) {
			cin >> out[j];
		}
		if (islegal(in, out, n)) {
			cout << "Yes" << endl;
		}
		else {
			cout << "No" << endl;
		}
	}
	return 0;
}