/*
Date:2021/5/4
动态规划
递归函数-超时
*/
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define inif 1000001

int t = 0;
vector<int> h;
vector<vector<int>> c;
int nn;
int dp(int i, int j, int k) {
	if (i < 0 || k < 0)
		return inif;
	if (k == 0 && i == 0) {
		if (h[i] == -1)
			return c[i][j];
		else if (h[i] == j)
			return 0;
		else
			return inif;
	}

	//此时可以保证只有k<= tartget && k>=1的情况下才会进入下面的代码块
	if (h[i] != -1 && j != h[i]) {
		return inif;
	}

	int min = inif;
	for (int j0 = 0; j0 < nn; j0++) {
		int res = 0;
		if (j == j0) {
			res = dp(i - 1, j, k);
		}
		else {
			res = dp(i - 1, j0, k - 1);
		}
		if (min > res)
			min = res;
	}
	if (h[i] == -1) {
		return min + c[i][j];
	}
	else {
		return min;
	}


}

int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
	t = target;
	c = cost;
	nn = n;
	for (int i = 0; i < houses.size(); i++) {
		h.push_back(houses[i] - 1);
	}
	vector<int> res(n);
	for (int i = 0; i < n; i++) {
		res[i] = dp(m-1, i, target-1);
	}
	sort(res.begin(), res.end());
	if (res[0] == inif)
		return -1;
	else
		return res[0];
}

int main() {
	vector<int> houses = { 0, 0, 0, 0, 0 };
	vector<vector<int>> cost = { {1, 10},{10, 1},{10, 1},{1, 10},{5, 1} };
	int m = 5, n = 2, target = 3;

	cout << minCost(houses, cost, m, n, target);
	return 0;
}