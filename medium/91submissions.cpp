/*
Date:2021/4/21
执行用时：0 ms
动态规划
f(n) = 
f(n-1)+f(n-2)  if 11<= s[n-1]s[n] <=26 && s[n] != 0 && s[n+1] != 0
f(n-1)         else
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int num(char c) {
	return c - '0';
}

int numDecodings(string s) {
	int len = s.length();
	vector<int> dp(len);
	if (s[0] == '0')
		return 0;
	if (len == 1)
		return 1;
	dp[0] = 1;
	for (int i = 1; i < len; i++) {
		if (s[i] == '0') {
			if (s[i - 1] != '1' && s[i - 1] != '2') {
				return 0;
			}
			dp[i - 1] = (i == 1 ? 1 : dp[i - 2]);
		}
		else {
			int twoDigit = num(s[i - 1]) * 10 + num(s[i]);
			if (twoDigit >= 11 && twoDigit <= 26 && s[i] != '0') {
				dp[i] = dp[i - 1] + (i == 1 ? 1 : dp[i - 2]);
				continue;
			}
		}
		dp[i] = dp[i - 1];
	
	}
	return dp[len-1];
}

int main() {
	cout << numDecodings("2101") << endl;//1
	cout << numDecodings("1123") << endl;//5
	cout << numDecodings("10") << endl;//1
	return 0;
}