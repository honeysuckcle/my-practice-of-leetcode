/*
Date:2021/5/4
动态规划-迭代
*/
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define inf 1000001

int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
	// 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
	for (int& c : houses) {
		--c;
	}

	// dp 所有元素初始化为极大值
	vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(target, inf)));

	for (int j = 0; j < n; j++) {
		if (houses[0] == -1)
			dp[0][j][0] = cost[0][j];
		else if (houses[0] == j)
			dp[0][j][0] = 0;
	}

	for (int i = 1; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (houses[i] != -1 && houses[i] != j) {
				continue;
			}

			for (int k = 0; k < target; k++) {
				for (int j0 = 0; j0 < n; j0++) {
					if (j == j0) {
						/*if (k == 0) {
							dp[i][j][k] = dp[i - 1][j][k];
						}*/
						dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k]);
					}
					else if (k != 0){
						dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1]);
					}
				}

				if (dp[i][j][k] != inf && houses[i] == -1) {
					dp[i][j][k] += cost[i][j];
				}
			}
		}
	}

	int res = inf;
	for (int j = 0; j < n; j++) {
		res = min(res, dp[m - 1][j][target - 1]);
	}
	return res == inf ? -1 : res;
}

int main() {
	vector<int> houses = { 0, 2, 1, 2, 0 };
	vector<vector<int>> cost = { {1, 10},{10, 1},{10, 1},{1, 10},{5, 1} };
	int m = 5, n = 2, target = 3;

	cout << minCost(houses, cost, m, n, target);
	return 0;
}