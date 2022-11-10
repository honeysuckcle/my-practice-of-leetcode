from collections import defaultdict
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def my_treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        high_dict= {}
        deep_dict = defaultdict(list)
        deep_node_dict = {}
        res_dict = {}
        def dfs(node, deep=0):
            if node is None:
                return 0
            left = dfs(node.left, deep+1)
            right = dfs(node.right, deep+1)
            high = max(left, right) + 1
            high_dict[node.val] = high
            deep_node_dict[node.val] = deep
            deep_dict[deep].append(node.val)
            return high
        dfs(root)
        for k in high_dict.keys():
            deep = deep_node_dict[k]
            higest = 0
            for node in deep_dict[deep]:
                if high_dict[node] > higest and node != k:
                    higest = high_dict[node]
            res_dict[k] = higest + deep
        res = []
        for q in queries:
            res.append(res_dict[q])
        
        return res

        