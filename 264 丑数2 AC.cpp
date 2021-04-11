/*
date��2021��4��11��
����һ��ʼ�õ���int������������ʾ���£�
Line 40: Char 12: runtime error: signed integer overflow: 429981696 * 5 cannot be represented in type 'int' (solution.cpp)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior prog_joined.cpp:49:12
֮���int�ĳ�long�Ϳ���ִ����

��������ﷸ���ĵͼ�����
1. �Ƚ���Сֵ�����ǱȽ����ֵ
2. ���ǰ��·ŵ�res��ֵ���䵽������

�����˼·��
һ��ʼ�õİ취��ĩβû�м�AC���ļ�������е�n=469��ʱ��ᳬʱ
������������ϣ��ο���https://zhuanlan.zhihu.com/p/67067455��ƪ�����еĽ��ⷽ��
����֪�ĳ����ֱ����2 3 5���ŵ����������ÿ�αȽϳ�����front��ֵ����Сֵ
����Сֵ��res��������ֵ�Ƚϣ�ע����е�ǰ�����Сֵ�Ѿ���res�����������������Ҫ���Ƚϣ�
�������С�Ϳ��Լ��뵽res������
res�����е������ǳ����ļ��ϣ�����Ϊ�˷��㣬�˷���res[0]��һ���ռ䣬index��1��ʼ
*/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

//�Ƚ��������������Сֵ�����Ұ���Сֵ�Լ���ͬ��pop��
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

//���µ�����䵽������
void push(queue<long> &q2, queue<long> &q3, queue<long> &q5, long i) {
	q2.push(i * 2);
	q3.push(i * 3);
	q5.push(i * 5);
}

long nthUglyNumber(long n) {
	if (n < 7) {
		return n;
	}
	vector<long> res(n+1); //res[n]��Ϊ�����res[0]����
	queue<long> q2, q3, q5;//*2 *3 *5���������

	long count = 6;//res���������ݵ����index
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