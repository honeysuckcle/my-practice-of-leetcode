/*
Date��2021-4-12
�����ľ�������cmp���������ⷽ����������Zfans�ṩ�ķ���

�����Ĵ���
һ��ʼû�а�cmp��������Ϊ��̬������������Ϣ���£�
Line 10: Char 40: error: reference to non-static member function must be called
		sort(nums.begin(), nums.end(), cmp);
									   ^~~
1 error generated.
ԭ������Ϊcmp��������Ϊ���Ա������ʱ��һ����Ҫstatic����
���������ڶ���ķ�static��Ա�����ھ����������ʽ��Ϊ���������һ��thisָ�����
����׼���sort()�����ĵ�����cmp����ָ������в�û������thisָ�����
��˻���������cmp������sort()Ҫ��Ĳ�����ƥ������
�����Ϊû��thisָ��ľ�̬��Ա�������Խ����һ����

������������Ĳ���������
1.
���룺
[0,0]
�����
"00"
Ԥ�ڽ����
"0"

2. 
���룺
[0]
�����
""
Ԥ�ڽ����
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
	sort(nums.begin(), nums.end(), cmp);//�õ��˿��ţ�������˲�������Ͷ�����ʱ�临�Ӷ�Ϊn*log(n)
	string res = "";
	for (int n : nums) {
		if (n != 0 || res[0] != '0')//��һ����Ҫ�����ڽ��δͨ����������������
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