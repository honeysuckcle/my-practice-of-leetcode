/*
Date: 2021/4/17
*/
#include<iostream>
#include<vector>
#include<math.h>
#include<set>
#include<algorithm>
#include<climits>
#include<unordered_map>
#include<queue>
using namespace std;

/*
版本一：
以下代码是最初始的解法，但是在下面的测试用例上遇到了问题：
用例1：
[-2147483648, 2147483647]
1
1
用例2：
[7,1,3]
2
3
*/

bool containsNearbyAlmostDuplicate1(vector<int>& nums, int k, int t) {
	for (int i = 0; i < nums.size() - k; i++) {
		for (int j = i+1; j <= i+k; j++) {
			if (abs(nums[i] - nums[j]) <= t)//int溢出
				return true;
		}
	}
	return false;
}

/*
版本二：
时间复杂度O(n^2),超出时间限制
*/
bool containsNearbyAlmostDuplicate2(vector<int>& nums, int k, int t) {
	for (int i = 0; i < nums.size(); i++) {
		for (int j = i + 1; j <= i + k && j < nums.size(); j++) {
			if (abs((long)nums[i] - (long)nums[j]) <= t) {
				return true;
			}
		}
	}
	return false;
}

/*
版本三：AC
滑动窗口算法，思路见最后
时间复杂度：O(nlog(min(n, k)))
空间复杂度：O(min(n, k))
*/
bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
	set<int> window;//滑动窗口，只存储当前元素的前k个元素
	if (nums.size() <= 0)
		return false;
	int x;//存当前元素
	for (int i = 0; i < nums.size(); i++) {
		x = nums[i];
		auto it = window.lower_bound(max(x,INT_MIN+t)-t);//查找集合中大于等于x-t的最小值
		if (it != window.end() && *it <= min(x,INT_MAX-t)+t)//如果查到了，并且该值小于等于x+t，返回true
			return true;
		window.insert(x);//无需处理返回结果，即使存在相同值，该值也只需要判断一次
		if (i >= k)
			window.erase(nums[i - k]);
	}
	return false;
}

/*
版本四：
利用桶排序的思想
时间复杂度：O(n)
空间复杂度：O(min(n,k))
该算法巧妙在unorder_map的运用上
另外：
[2147483647,-1,2147483647]
1
2147483647
这个测试用例真的绝了
*/
int get_a(int x, long s) {
	int a = x / s;
	return (x < 0 && x%s != 0) ? a - 1 : a;
}
bool containsNearbyAlmostDuplicate4(vector<int>& nums, int k, int t) {
	//每个数x可以表示为x=(t+1)a+b(0<=b<=t)
	//a是桶的序号，桶内放x
	unordered_map<int, int> map;//桶，容量为t+1

	for (int i = 0; i < nums.size(); i++) {
		int a = get_a(nums[i], t + 1ll);

		//存在桶a，并且满足桶里面的数和i相差在k以内
		if (map.count(a) > 0) {
			return true;
		}
		//查看相邻的桶
		if (map.count(a - 1) > 0 && abs((long)map[a - 1] - nums[i]) <= t) {
			return true;
		}
		if (map.count(a + 1) > 0 && abs((long)map[a + 1] - nums[i]) <= t) {
			return true;
		}
		//更新桶里的数据，保证只有下标在[i-k,i]区间的数据在里面
		map[a] = nums[i];
		if (i >= k) {
			map.erase(get_a(nums[i - k], t + 1ll));
		}

	}
	return false;
}

int main() {
	//这个程序中有不少极端的测试用例，存在溢出情况
	cout << (long)-2147483641 - 100 << endl;//2147483555
	cout << (long)2147483641 + 100 << endl;//-2147483555
	cout << 2147483647 + 1 << endl;//-2147483648
	cout << (long)2147483647 + 1 << endl;//-2147483648

	//桶排序中负数要做特别处理
	cout << -3 / 2 << endl;
	cout << -3 % 3 << endl;

	vector<int> nums;
	char c = cin.get();
	while (c != ']') {
		int i;
		cin >> i;
		nums.push_back(i);
		c = cin.get();
	}
	int k = 1, t = 1;
	cin >> k >> t;
	cout << containsNearbyAlmostDuplicate(nums, k, t) << endl;
	cout << containsNearbyAlmostDuplicate4(nums, k, t) << endl;
	return 0;
}

/*
滑动窗口算法思路：

对于序列中每一个元素 xx 左侧的至多 kk 个元素，如果这 kk 个元素中存在一个元素落在区间 [x - t, x + t][x−t,x+t] 中，我们就找到了一对符合条件的元素。注意到对于两个相邻的元素，它们各自的左侧的 kk 个元素中有 k - 1k−1 个是重合的。于是我们可以使用滑动窗口的思路，维护一个大小为 kk 的滑动窗口，每次遍历到元素 xx 时，滑动窗口中包含元素 xx 前面的最多 kk 个元素，我们检查窗口中是否存在元素落在区间 [x - t, x + t][x−t,x+t] 中即可。

如果使用队列维护滑动窗口内的元素，由于元素是无序的，我们只能对于每个元素都遍历一次队列来检查是否有元素符合条件。如果数组的长度为 nn，则使用队列的时间复杂度为 O(nk)O(nk)，会超出时间限制。

因此我们希望能够找到一个数据结构维护滑动窗口内的元素，该数据结构需要满足以下操作：

支持添加和删除指定元素的操作，否则我们无法维护滑动窗口；

内部元素有序，支持二分查找的操作，这样我们可以快速判断滑动窗口中是否存在元素满足条件，具体而言，对于元素 xx，当我们希望判断滑动窗口中是否存在某个数 yy 落在区间 [x - t, x + t][x−t,x+t] 中，只需要判断滑动窗口中所有大于等于 x - tx−t 的元素中的最小元素是否小于等于 x + tx+t 即可。

我们可以使用有序集合来支持这些操作。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/contains-duplicate-iii/solution/cun-zai-zhong-fu-yuan-su-iii-by-leetcode-bbkt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/