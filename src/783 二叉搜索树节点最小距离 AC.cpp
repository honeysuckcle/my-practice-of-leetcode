/*Date:2021/4/13

完成了支持完整输入输出的程序，包括如下部分：
1. 根据[98,78,null,66,79]这种格式的输入构建BST
2. 打印BST
3. 计算最小距离并输出
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

 //一些与解题无关的工具函数（只是为了让这个cpp可以运行，于是编写了构建BST的部分）
 vector<string> split(const string& str, const string& delim);
 void printTree(TreeNode *root);

 //---------------------------------
 //从这里开始是需要复制到leetcode的代码
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
	 getline(cin, str);//读取一行字符串
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
  版权声明：下面的函数出自为CSDN博主「海阔天空sky1992」的原创文章。
  原文链接：https ://blog.csdn.net/Mary19920410/article/details/77372828

  此函数用于树的构建，不需要复制到leetcode中
 */
 vector<string> split(const string& str, const string& delim) {
	 vector<string> res;
	 if ("" == str) return res;
	 //先将要切割的字符串从string类型转换为char*类型
	 char * strs = new char[str.length() + 1]; //不要忘了
	 strcpy(strs, str.c_str());

	 char * d = new char[delim.length() + 1];
	 strcpy(d, delim.c_str());

	 char *p = strtok(strs, d);
	 while (p) {
		 string s = p; //分割得到的字符串转换为string类型
		 res.push_back(s); //存入结果数组
		 p = strtok(NULL, d);
	 }

	 return res;
 }

 /*
 以下两个函数用于打印二叉树
 版权声明：本文为CSDN博主「fxxxkming」的原创文章，遵循CC 4.0 BY - SA版权协议，转载请附上原文出处链接及本声明。
 原文链接：https ://blog.csdn.net/weixin_41990671/article/details/108885298
*/

 /**
  * 中序遍历返回节点数组
  * @param root 根节点
  * @return 中序遍历节点数组
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
 * 利用下划线和正反斜杠打印出美观的二叉树，没有破坏二叉树结构，但传入的root会有变化
 * @param root  二叉树根节点
 */
 void printTree(TreeNode *root) {
	 if (!root)return;
	 auto tmp = root;
	 vector<TreeNode *> intv = inorderTraversal(tmp);//中序遍历节点数组
	 string template_str;//模板string，表示每行打印string的长度
	 int location = 0;
	 unordered_map<TreeNode *, int> first_locations;//存储节点对应在本行string中的首位置
	 for (auto &i : intv) {
		 location = template_str.size();
		 template_str += to_string(i->val) + " ";
		 first_locations[i] = location;
	 }
	 for (auto &i : template_str)i = ' ';//把模板全部置为空格方便后续使用
	 //层序遍历
	 queue<TreeNode *> q;
	 q.push(root);
	 while (!q.empty()) {
		 int currentLevelSize = q.size();
		 int cur_loc = 0;
		 string tmp_str1 = template_str, tmp_str2 = template_str;//1为节点所在行，2为其下一行
		 for (int i = 1; i <= currentLevelSize; ++i) {
			 auto node = q.front();
			 q.pop();
			 cur_loc = first_locations[node];
			 string num_str = to_string(node->val);
			 //左边，如果存在左孩子，那么在第二行对应位置打印'/'，在第一行补上'_'
			 if (node->left) {
				 q.push(node->left);
				 int first_loc = first_locations[node->left] + 1;
				 tmp_str2[first_loc++] = '/';
				 while (first_loc < cur_loc)tmp_str1[first_loc++] = '_';

			 }
			 //中间,对应位置打印节点值（有可能为多位数）
			 for (int j = 0; j < num_str.length(); ++j, ++cur_loc) {
				 tmp_str1[cur_loc] = num_str[j];
			 }
			 //右边，如果存在右孩子，那么在第二行对应位置打印'\'，在第一行补上'_'
			 if (node->right) {
				 q.push(node->right);
				 int last_loc = first_locations[node->right] - 1;
				 tmp_str2[last_loc] = '\\';
				 while (cur_loc < last_loc) {
					 tmp_str1[cur_loc++] = '_';
				 }
			 }
		 }
		 //打印两行
		 cout << tmp_str1 << endl;
		 cout << tmp_str2 << endl;
	 }
 }

