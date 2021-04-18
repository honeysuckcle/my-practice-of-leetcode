/*
Date:2021/4/18
��Ŀ������
ɾ��һ�������������ظ������֣�Ҫ��ռ临�Ӷ�O(1)
�㷨˼·��
��Ϊ����������ģ�ֱ�ӽ���������鸳ֵ���ظ��ĵڶ������ֵ�λ�ü��ɣ�
Ҳ����˵��ÿ����ֻ����һ��
�ٽ��޸Ĺ���������ĺ���Ķ��������ɾ������
*/

#include<iostream>
#include<vector>
using namespace std;

//�ҵĴ��� AC
int removeDuplicates(vector<int>& nums) {
	if (nums.size() == 0)
		return 0;
	int p = 0;//�޸Ĺ�����������±����ֵ
	//
	for (int i = 0; i < nums.size(); i++) {
		if (nums[i] != nums[p]) {
			nums[++p] = nums[i];
		}
	}
	//ɾ�����������
	while (nums.size() >= 0 && nums.size() - 1 != p) {
		nums.pop_back();
	}
	return p + 1;
}

//�ٷ���� �ο�����
//�Ҹо��ٷ���Ⲣû�����ɾ����������������׺��
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