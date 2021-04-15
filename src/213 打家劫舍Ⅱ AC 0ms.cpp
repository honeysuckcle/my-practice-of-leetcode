/*
Date:2021/4/15
算法：动态规划
状态转移函数：dp[i]=max(dp[i−2]+nums[i],dp[i−1])
*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

//此处没有用dp数组做动态规划，而是使用两个整型ab来记录dp[i-2]和dp[i-1]
//start:起始index
//end:终止位置的index+1
int dp(vector<int>& nums, int start, int end) {
	int a=nums[start], b=max(nums[start],nums[start+1]);
	int res = max(a,b);
	for (int i = start+2; i < end; i++) {
		res = max(a + nums[i], b);
		a = b;
		b = res;
	}
	return res;
}

//将一个问题分为两个问题，来解决收尾相连的问题
//即计算dp(nums, 0, len - 1)和dp(nums, 1, len)，取最大值
int rob(vector<int>& nums) {
	int len = nums.size();
	if (len == 1)
		return nums[0];
	if (len == 2)
		return max(nums[0], nums[1]);
	int a = dp(nums, 0, len - 1), b = dp(nums, 1, len);
	return max(a, b);
}

int main() {
	vector<int> nums = { 1,2,3,1 };
	cout << rob(nums);
	return 0;
}