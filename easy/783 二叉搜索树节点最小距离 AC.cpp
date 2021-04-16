/*Date:2021/4/13

�����֧��������������ĳ��򣬰������²��֣�
1. ����[98,78,null,66,79]���ָ�ʽ�����빹��BST
2. ��ӡBST
3. ������С���벢���
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<unordered_map>
using namespace std;

 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

 //һЩ������޹صĹ��ߺ�����ֻ��Ϊ�������cpp�������У����Ǳ�д�˹���BST�Ĳ��֣�
 vector<string> split(const string& str, const string& delim);
 void printTree(TreeNode *root);

 //---------------------------------
 //�����￪ʼ����Ҫ���Ƶ�leetcode�Ĵ���
 TreeNode* pre(TreeNode *root) {
	 TreeNode * curr = root->left;
	 while (curr != nullptr && curr->right != nullptr) {
		 curr = curr->right;
	 }
	 return curr;
 }

 TreeNode * next(TreeNode * root) {
	 TreeNode * curr = root->right;
	 while (curr != nullptr && curr->left != nullptr) {
		 curr = curr->left;
	 }
	 return curr;
 }
 
 int minDiffInBST(TreeNode* root) {
	 if (root->left == nullptr) {
		 if (root->right == nullptr) {
			 return 999999999;
		 }
		 else
			 return min((next(root)->val) - (root->val), minDiffInBST(root->right));
	 }
	 else {
		 if (root->right == nullptr) {
			 return min((root->val) - (pre(root)->val), minDiffInBST(root->left));
		 }
		 else {
			 int a = (root->val) - (pre(root)->val);
			 int b = (next(root)->val) - (root->val);
			 return min(min(a, b), min(minDiffInBST(root->left), minDiffInBST(root->right)));
		 }
	 }
 }
 //---------------------------------
 //end

 TreeNode *build(vector<string> s) {
	 int len = s.size();
	 TreeNode * root = new TreeNode();
	 if (len > 0 && s[0] != "null")
		 root->val = stoi(s[0]);
	 else
		 return root;
	 queue<TreeNode*> q;
	 int count = 1;
	 q.push(root);
	 while (!q.empty() && count < len) {
		 TreeNode* curr = q.front();
		 if (s[count++] != "null") {
			 curr->left = new TreeNode(stoi(s[count-1]));
			 q.push(curr->left);
			 
		 }
		 if (s[count++] != "null") {
			 curr->right = new TreeNode(stoi(s[count-1]));
			 q.push(curr->right);
		 }
		 q.pop();
	 }
	 return root;
 }

 int main() {
	 string str;
	 getline(cin, str);//��ȡһ���ַ���
	 vector<string> nodes = split(str, "[],");

	 //display
	 /*for (string s : nodes) {
		 cout << s << endl;
	 }*/

	 TreeNode *root = build(nodes);
	 printTree(root);

	 cout <<"minDiffInBST: " <<minDiffInBST(root) << endl;
	 
	 return 0;
 }

 /*
  ��Ȩ����������ĺ�������ΪCSDN�������������sky1992����ԭ�����¡�
  ԭ�����ӣ�https ://blog.csdn.net/Mary19920410/article/details/77372828

  �˺����������Ĺ���������Ҫ���Ƶ�leetcode��
 */
 vector<string> split(const string& str, const string& delim) {
	 vector<string> res;
	 if ("" == str) return res;
	 //�Ƚ�Ҫ�и���ַ�����string����ת��Ϊchar*����
	 char * strs = new char[str.length() + 1]; //��Ҫ����
	 strcpy(strs, str.c_str());

	 char * d = new char[delim.length() + 1];
	 strcpy(d, delim.c_str());

	 char *p = strtok(strs, d);
	 while (p) {
		 string s = p; //�ָ�õ����ַ���ת��Ϊstring����
		 res.push_back(s); //����������
		 p = strtok(NULL, d);
	 }

	 return res;
 }

 /*
 ���������������ڴ�ӡ������
 ��Ȩ����������ΪCSDN������fxxxkming����ԭ�����£���ѭCC 4.0 BY - SA��ȨЭ�飬ת���븽��ԭ�ĳ������Ӽ���������
 ԭ�����ӣ�https ://blog.csdn.net/weixin_41990671/article/details/108885298
*/

 /**
  * ����������ؽڵ�����
  * @param root ���ڵ�
  * @return ��������ڵ�����
  */
 vector<TreeNode *> inorderTraversal(TreeNode *root) {
	 vector<TreeNode *> res;
	 stack<TreeNode *> stk;
	 while (root != nullptr || !stk.empty()) {
		 while (root != nullptr) {
			 stk.push(root);
			 root = root->left;
		 }
		 root = stk.top();
		 stk.pop();
		 res.push_back(root);
		 root = root->right;
	 }
	 return res;
 }


 /**
 * �����»��ߺ�����б�ܴ�ӡ�����۵Ķ�������û���ƻ��������ṹ���������root���б仯
 * @param root  ���������ڵ�
 */
 void printTree(TreeNode *root) {
	 if (!root)return;
	 auto tmp = root;
	 vector<TreeNode *> intv = inorderTraversal(tmp);//��������ڵ�����
	 string template_str;//ģ��string����ʾÿ�д�ӡstring�ĳ���
	 int location = 0;
	 unordered_map<TreeNode *, int> first_locations;//�洢�ڵ��Ӧ�ڱ���string�е���λ��
	 for (auto &i : intv) {
		 location = template_str.size();
		 template_str += to_string(i->val) + " ";
		 first_locations[i] = location;
	 }
	 for (auto &i : template_str)i = ' ';//��ģ��ȫ����Ϊ�ո񷽱����ʹ��
	 //�������
	 queue<TreeNode *> q;
	 q.push(root);
	 while (!q.empty()) {
		 int currentLevelSize = q.size();
		 int cur_loc = 0;
		 string tmp_str1 = template_str, tmp_str2 = template_str;//1Ϊ�ڵ������У�2Ϊ����һ��
		 for (int i = 1; i <= currentLevelSize; ++i) {
			 auto node = q.front();
			 q.pop();
			 cur_loc = first_locations[node];
			 string num_str = to_string(node->val);
			 //��ߣ�����������ӣ���ô�ڵڶ��ж�Ӧλ�ô�ӡ'/'���ڵ�һ�в���'_'
			 if (node->left) {
				 q.push(node->left);
				 int first_loc = first_locations[node->left] + 1;
				 tmp_str2[first_loc++] = '/';
				 while (first_loc < cur_loc)tmp_str1[first_loc++] = '_';

			 }
			 //�м�,��Ӧλ�ô�ӡ�ڵ�ֵ���п���Ϊ��λ����
			 for (int j = 0; j < num_str.length(); ++j, ++cur_loc) {
				 tmp_str1[cur_loc] = num_str[j];
			 }
			 //�ұߣ���������Һ��ӣ���ô�ڵڶ��ж�Ӧλ�ô�ӡ'\'���ڵ�һ�в���'_'
			 if (node->right) {
				 q.push(node->right);
				 int last_loc = first_locations[node->right] - 1;
				 tmp_str2[last_loc] = '\\';
				 while (cur_loc < last_loc) {
					 tmp_str1[cur_loc++] = '_';
				 }
			 }
		 }
		 //��ӡ����
		 cout << tmp_str1 << endl;
		 cout << tmp_str2 << endl;
	 }
 }

