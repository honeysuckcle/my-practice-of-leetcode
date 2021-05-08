/*
Date:2021/5/8
经典动态规划问题
如果采用贪心算法，会在下面的测试用例出问题
[5,5,4,4,4]
2

官方解题方法有很多巧思，比如：
1. 用int的二进制表示已分配工作的集合
2. j-x 表示j为全集时，x的补集
3. for(int x=j; x; x = (x-1) & j) 其中x是j的子集

*/
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int minimumTimeRequired(vector<int>& jobs, int k) {
	int n = pow(2, jobs.size());
	vector<int> sum(n);
	for (int i = 0; i < n; i++) {
		int t = i;
		for (int j = jobs.size()-1; j >= 0 && t >= 0; j--) {
			int tail = t % 2;
			t /= 2;
			sum[i] += tail ? jobs[j] : 0;
		}
	}

	vector<vector<int>> dp(k, vector<int>(n));//size: k*(2^n-1)

	for (int i = 0; i < n; i++) {
		dp[0][i] = sum[i];
	}

	for (int i = 1; i < k; i++) {
		for (int j = 1; j < n; j++) {
			int min = INT_MAX;
			for (int t = j; t > 0 ; t = (t-1) & j) {
				int time = max(dp[i - 1][j - t], sum[t]);
				min = time < min ? time : min;
			}
			dp[i][j] = min;
		}
	}

	return dp[k - 1][n - 1];

}

int main() {
	vector<int> jobs = { 3,2,3 };
	int k =3;
	cout << minimumTimeRequired(jobs, k);
	return 0;
}