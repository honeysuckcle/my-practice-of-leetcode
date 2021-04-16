/*
Date: 2021-4-16

һ��ʼ��˼·�ر�򵥣�
��Ϊs1 �� s2 ��СдӢ����ĸ���
������������Ϊ26�����飬�ֱ�洢�����ַ����и�����ĸ���ֵĴ���
�Ƚ����������飬���һ���ͷ���true�����򷵻�false
��������Ȼ�͹�������Ѷ�Ϊhard����Ŀ����û��ͨ�����²���������
���룺
"abcde"
"caebd"
�����
true
Ԥ�ڽ����
false

��Ҫʹ�ö�̬�滮�㷨
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
//x:s1��ʼ��y:s2��ʼ��len:���ַ�������
//-1 ��ʾ false��1 ��ʾ true��0 ��ʾδ����
int dp[30][30][31];
bool dp_fun(string &s1, string &s2, int x, int y, int len) {

	//����д𰸾�ֱ�ӷ���
	if (dp[x][y][len] != 0)
		return dp[x][y][len] == 1;

	//���������Ӵ��Ƿ����
	if (s1.substr(x, len) == s2.substr(y, len)) {
		dp[x][y][len] = 1;
		return true;
	}

	//�ж������ַ����е���ĸ��������Ƿ���ͬ
	if (!compareList(s1.substr(x, len), s2.substr(y, len))) {
		dp[x][y][len] = -1;
		return false;
	}

	//ö�ٷָ�λ��
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