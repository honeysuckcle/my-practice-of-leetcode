"""
Date: 2021/9/5
用随机解决随机
"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return (rand7() + rand7() + rand7() + rand7() + rand7()) % 10 + 1