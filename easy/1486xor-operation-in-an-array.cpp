/*
Date:2021/5/7
*/
#include<iostream>
using namespace std;

int xorOperation(int n, int start) {
	int res = start;
	for (int i = 1; i < n; i++) {
		res ^= start + i * 2;
	}
	return res;
}

int main() {

	cout << xorOperation(5,0);
	return 0;
}