# my-practice-of-leetcode

这是一个记录每天刷leetcode的题目的repo；

计划从2021年4月11日开始每日一题；

题目选择为leetcode自动推荐的每日一题，因此是随机的；

解题思路等文字放在代码开头的注释中；

恳请大家批评指正！


### 题目难度——简单

[783. 二叉搜索树节点最小距离 minimum-distance-between-bst-nodes](https://github.com/honeysuckcle/my-practice-of-leetcode/blob/main/783%20%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%8A%82%E7%82%B9%E6%9C%80%E5%B0%8F%E8%B7%9D%E7%A6%BB%20AC.cpp)
这道题和第530题要解决的问题相同

![783 运行截图](pic/783.jpg)


### 题目难度——中等

[179. 最大数 largest-number](https://github.com/honeysuckcle/my-practice-of-leetcode/blob/main/179%20%E6%9C%80%E5%A4%A7%E6%95%B0%20AC.cpp)

[208. 实现Trie implement-trie-prefix-tree](https://github.com/honeysuckcle/my-practice-of-leetcode/blob/main/208%20%E5%AE%9E%E7%8E%B0Trie%20AC.cpp)

[213. 打家劫舍 house-robber-ii](https://github.com/honeysuckcle/my-practice-of-leetcode/blob/main/src/213%20%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D%E2%85%A1%20AC%200ms.cpp)

[264. 丑数Ⅱ ugly-number-ii](https://github.com/honeysuckcle/my-practice-of-leetcode/blob/main/264%20%E4%B8%91%E6%95%B02%20AC.cpp)

### 题目难度——困难

[87. 扰乱字符串 scramble-string](/hard/scramble-string.cpp)
动态规划——转移方程：
$$
f(s_1,s_2)= ⋁_{i=1}^{n−1}(f(s_1[0,i],s_2[0,i])∧f(s_1[i,n−i],s_2[i,n−i]))\\
或⋁_{i=1}^{n−1}(f(s_1[0,i],s_2[n-i,i])∧f(s_1[i,n−i],s_2[0,n−i]))
$$

其中：n表示s1.length==s2.length，*s*1(*x*,*y*) 表示从 *s*1 从第 x个字符（从 0开始编号）开始，长度为 y的子串