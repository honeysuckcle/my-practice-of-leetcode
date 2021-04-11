/*
date：2021年4月11日
程序一开始用的是int，报错，错误提示如下：
Line 40: Char 12: runtime error: signed integer overflow: 429981696 * 5 cannot be represented in type 'int' (solution.cpp)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior prog_joined.cpp:49:12
之后把int改成long就可以执行了

这个代码里犯过的低级错误：
1. 比较最小值，不是比较最大值
2. 忘记把新放到res的值补充到队列里

代码的思路：
一开始用的办法在末尾没有加AC的文件里，它运行到n=469的时候会超时
因此上网查资料，参考了https://zhuanlan.zhihu.com/p/67067455这篇文章中的解题方法
把已知的丑数分别乘以2 3 5，放到三个队列里，每次比较出三个front的值的最小值
把最小值和res数组的最大值比较（注意会有当前这个最小值已经在res数组里的情况，因此需要作比较）
如果比它小就可以加入到res数组中
res数组中的数就是丑数的集合，这里为了方便，浪费了res[0]这一个空间，index从1开始
*/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

//比较三个队列里的最小值，并且把最小值以及相同数pop掉
long min(queue<long> &q1, queue<long> &q2, queue<long> &q3) {
	long a = q1.front(), b = q2.front(), c = q3.front();
	if (a < b) {
		if (a < c) {
			q1.pop();
			return a;
		}
		else {
			q3.pop();
			if (a == c) {
				q1.pop();
			}
			return c;
		}
	}
	else {
		if (b < c) {
			q2.pop();
			if (a == b) {
				q1.pop();
			}
			return b;
		}
		else {
			q3.pop();
			if (b == c) {
				q2.pop();
			}
			return c;
		}
	}
}

//将新的数填充到队列里
void push(queue<long> &q2, queue<long> &q3, queue<long> &q5, long i) {
	q2.push(i * 2);
	q3.push(i * 3);
	q5.push(i * 5);
}

long nthUglyNumber(long n) {
	if (n < 7) {
		return n;
	}
	vector<long> res(n+1); //res[n]即为结果，res[0]无用
	queue<long> q2, q3, q5;//*2 *3 *5的三组队列

	long count = 6;//res中已有数据的最大index
	for (long i = 1; i <= 6; i++) {
		res[i] = i;
		push(q2, q3, q5, i);
	}

	while (count < n) {
		long m = min(q2, q3, q5);
		while (m <= res[count]) {
			m = min(q2, q3, q5);
		}
		res[count + 1] = m;
		push(q2, q3, q5, m);
		count++;
	}

	//display
	/*for (int i = 1; i < res.size(); i++) {
		cout << i <<" "<<res[i] << endl;
	}*/
	return res[n];
}

int main() {
	int n;
	cin >> n;
	cout << nthUglyNumber(n) << endl;
	return 0;
}