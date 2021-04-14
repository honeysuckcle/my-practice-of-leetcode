/*
Date：2021-4-12
这道题的精髓在于cmp函数，解题方法是评论区Zfans提供的方法

犯过的错误：
一开始没有把cmp函数设置为静态函数，报错信息如下：
Line 10: Char 40: error: reference to non-static member function must be called
		sort(nums.begin(), nums.end(), cmp);
									   ^~~
1 error generated.
原因是因为cmp函数在作为类成员函数的时候一定需要static修饰
所有在类内定义的非static成员函数在经过编译后隐式的为他们添加了一个this指针参数
而标准库的sort()函数的第三个cmp函数指针参数中并没有这样this指针参数
因此会出现输入的cmp参数和sort()要求的参数不匹配的情况
将其改为没有this指针的静态成员函数可以解决这一问题

部分遇到问题的测试用例：
1.
输入：
[0,0]
输出：
"00"
预期结果：
"0"

2. 
输入：
[0]
输出：
""
预期结果：
"0"
*/


#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

static bool cmp(int a, int b) {
	string sa = to_string(a);
	string sb = to_string(b);
	return sa + sb > sb + sa; //core
}

string largestNumber(vector<int>& nums) {
	sort(nums.begin(), nums.end(), cmp);//用到了快排，并结合了插入排序和堆排序，时间复杂度为n*log(n)
	string res = "";
	for (int n : nums) {
		if (n != 0 || res[0] != '0')//这一行主要是用于解决未通过的两个测试用例
			res += to_string(n);
	}
	return res;
}

int main() {
	vector<int> arr;
	char c;
	int n;
	c = cin.get();
	while (c != ']') {
		cin >> n;
		arr.push_back(n);
		c = cin.get();
	}
	cout << largestNumber(arr);
	return 0;
}