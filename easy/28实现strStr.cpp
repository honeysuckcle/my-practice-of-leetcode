/*
Date:2021/4/20
KMP算法，减少重复比较，时间复杂度O(m+n)
建议先写暴力算法，然后思考改进策略，之后自然而然地就理解kmp算法的思想了
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;

/*
判断当前k如果不符合情况的话，k可以变成几，使得重复比较的次数最少
*/
vector<int> skip(string needle) {
	int len = needle.length();
	vector<int> next(len);
	int j = 0, k = -1;
	next[0] = -1;
	while (j < len - 1)
	{
		if (k == -1 || needle[j] == needle[k])
		{
			j++; k++;
			next[j] = k;
		}
		else k = next[k];
	}
	return next;
}

int strStr(string haystack, string needle) {
	//如果needle为空字符串，返回0
	if (needle.length() == 0)
		return 0;
	int i = 0, k = 0;
	vector<int> next = skip(needle);
	for (int i : next) {
		cout << i << " ";
	}
	int hl = haystack.length();
	int nl = needle.length();
	cout << "\n" << hl<<" "<<nl << endl;
	while(i<hl && k <nl) {
			if (k == -1 || haystack[i] == needle[k]) {
				if (k == needle.length() - 1) {
					return i - needle.length()+1;
				}
				i++;
				k++;
			}
			else {
				k = next[k];
			}
	
	}
	return -1;
}

int main() {
	cout << strStr("helloworld", "ll") << endl;
	cout << strStr("aaaaa", "bba") << endl;
	cout << strStr("mississippi","issip") << endl;
	cout << strStr("mississippi", "issi") << endl;
	return 0;
}

/*
解答此题时遗留几个问题，今天时间不够，之后解决：
1. 第19行原本写的是k<needle.length()，但是当k=-1的时候，该语句判为false？？？
2. 构建next数组的时候while(j<len-1)不符合我的习惯，能否修改代码实现j<len,并且得到正确的next数组
3. kmp存在优化算法
*/