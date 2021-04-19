/*
Date:2021/4/19
和上一题十分类似,使用快慢指针
*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int removeElement(vector<int>& nums, int val) {
	sort(nums.begin(), nums.end());
	int slow = 0, fast = 0;
	while (fast < nums.size()) {
		if (nums[fast] < val) {
			fast++;
			slow++;
		}
		else if (nums[fast] == val) {
			fast++;
		}
		else {
			nums[slow++] = nums[fast++];
		}
	}
	return slow;
}

int main() {
	vector<int> nums = { 0,0,1,1,1,2,2,3,3,4 };
	cout << removeElement(nums,3) << " nums=[";
	for (int x : nums) {
		cout << x << ",";
	}
	cout << "]" << endl;

	return 0;
}