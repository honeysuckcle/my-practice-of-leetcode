/*
Date: 2021-4-16

一开始的思路特别简单：
因为s1 和 s2 由小写英文字母组成
构造两个长度为26的数组，分别存储两个字符串中各个字母出现的次数
比较这两个数组，如果一样就返回true，否则返回false
但是我显然低估了这道难度为hard的题目，它没能通过如下测试用例：
输入：
"abcde"
"caebd"
输出：
true
预期结果：
false

需要使用动态规划算法
*/
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

bool compareList(string s1, string s2) {
	int list[2][26];
	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < 2; j++) {
			list[j][i] = 0;
		}
	}
	for (int i = 0; i < s1.length(); i++) {
		list[0][s1[i] - 'a']++;
		list[1][s2[i] - 'a']++;
	}
	bool flag = true;
	for (int i = 0; i < 26; i++) {
		if (list[0][i] != list[1][i]) {
			flag = false;
			break;
		}
	}
	return flag;
}

//dp[x][y][len]
//x:s1起始，y:s2起始，len:子字符串长度
//-1 表示 false，1 表示 true，0 表示未计算
int dp[30][30][31];
bool dp_fun(string &s1, string &s2, int x, int y, int len) {

	//如果有答案就直接返回
	if (dp[x][y][len] != 0)
		return dp[x][y][len] == 1;

	//计算两个子串是否相等
	if (s1.substr(x, len) == s2.substr(y, len)) {
		dp[x][y][len] = 1;
		return true;
	}

	//判断两个字符串中的字母及其个数是否相同
	if (!compareList(s1.substr(x, len), s2.substr(y, len))) {
		dp[x][y][len] = -1;
		return false;
	}

	//枚举分割位置
	for (int i = 1; i < len; i++) {
		if (dp_fun(s1, s2, x, y, i) && dp_fun(s1, s2, x + i, y + i, len - i)) {
			dp[x][y][len] == 1;
			return true;
		}
		if (dp_fun(s1, s2, x, y+len-i, i) && dp_fun(s1, s2, x + i, y, len - i)) {
			dp[x][y][len] == 1;
			return true;
		}
	}

	dp[x][y][len] = -1;
	return false;
}

bool isScramble(string s1, string s2) {

	if (!compareList(s1, s2))
		return false;

	memset(dp, 0, sizeof(dp));
	return dp_fun(s1, s2, 0, 0, s1.length());
}

int main() {
	string s1 = "xstjzkfpkggnhjzkpfjoguxvkbuopi", s2 = "xbouipkvxugojfpkzjhnggkpfkzjts";
	cout << isScramble(s1, s2);
}