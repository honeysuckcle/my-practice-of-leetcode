/*
Date:2021/4/18
题目描述：
删除一个升序数组中重复的数字，要求空间复杂度O(1)
算法思路：
因为数组是升序的，直接将更大的数组赋值到重复的第二个数字的位置即可，
也就是说，每个数只保留一个
再将修改过的子数组的后面的多余的数字删掉即可
*/

#include<iostream>
#include<vector>
using namespace std;

//我的代码 AC
int removeDuplicates(vector<int>& nums) {
	if (nums.size() == 0)
		return 0;
	int p = 0;//修改过的子数组的下标最大值
	//
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] != nums[p]) {
			nums[++p] = nums[i];
		}
	}
	//删除多余的数字
	while (nums.size() >= 0 && nums.size() - 1 != p) {
		nums.pop_back();
	}
	return p + 1;
}

//官方题解 参考代码
//我感觉官方题解并没有完成删除任务，数组后面会有缀余
int removeDuplicates_og(vector<int>& nums) {
	int n = nums.size();
	if (n == 0) {
		return 0;
	}
	int fast = 1, slow = 1;
	while (fast < n) {
		if (nums[fast] != nums[fast - 1]) {
			nums[slow] = nums[fast];
			++slow;
		}
		++fast;
	}
	return slow;
}


int main() {
	vector<int> nums = { 0,0,1,1,1,2,2,3,3,4 };
	cout << removeDuplicates_og(nums) << " nums=[";
	for (int x : nums) {
		cout << x << ",";
	}
	cout << "]" << endl;

	nums = { 0,0,1,1,1,2,2,3,3,4 };
	cout << removeDuplicates(nums) << " nums=[";
	for (int x : nums) {
		cout << x << ",";
	}
	cout << "]" << endl;
	return 0;
}