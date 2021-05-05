/*
Date:2021/5/5
动态规划
打家劫舍的变形版本
*/
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int deleteAndEarn(vector<int>& nums) {
	vector<int> sum;
	sort(nums.begin(), nums.end());

	int pre = -1;
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] != pre) {
			for (int j = 0; j < nums[i] - pre; j++) {
				sum.push_back(0);
			}
			pre = nums[i];
		}
		sum[pre] += pre;
	}

	vector<int> dp(sum.size());
	dp[0] = sum[0];
	dp[1] = max(sum[0], sum[1]);
	for (int i = 2; i < sum.size(); i++) {
		dp[i] = max(sum[i] + dp[i - 2], dp[i - 1]);
	}
	return dp[sum.size()-1];
}

int main() {
	vector<int> nums = { 3,4,2 };

	cout << deleteAndEarn(nums);
	return 0;
}