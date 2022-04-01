#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (40.91%)
# Likes:    1825
# Dislikes: 0
# Total Accepted:    642.1K
# Total Submissions: 1.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
# 示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
# 提示：
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
#
#
#

# @lc code=start

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         def isCommonPrefix(length):
#             base = strs[0][:length]
#             cnt = len(strs)
#             return all(base == strs[i][:length] for i in range(1, cnt))

        
#         if not strs:
#             return ""
        
#         min_length = min(len(s) for s in strs)
#         low, high = 0, min_length
#         while low < high:
#             mid = (high - low) // 2 + low
#             if isCommonPrefix(mid):
#                 low = mid
#             else:
#                 high = mid - 1

#         return strs[0][:low]


# # 对列表中第一个单词的内容做二分查找
# # 36ms 50.9%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        def isCommonPrefix(length):
            base, cnt = strs[0][:length], len(strs)
            return all(strs[i][:length] == base for i in range(1, cnt))

        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        low, high = 0, min_length
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
        
        return strs[0][:low]


# # 分治 32ms 76%
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         def _longestCommonPrefix(start, end):
#             if start == end:
#                 return strs[start]

#             mid = (start + end) // 2
#             lcp_left, lcp_right = _longestCommonPrefix(start, mid), _longestCommonPrefix(mid + 1, end)

#             min_length = min(len(lcp_left), len(lcp_right))
#             for i in range(min_length):
#                 if lcp_left[i] != lcp_right[i]:
#                     return lcp_left[:i]
#             return lcp_left[:min_length]

#         return "" if not strs else _longestCommonPrefix(0, len(strs) -1)


# # 横向对比 36ms 50%
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         prefix, cnt = strs[0], len(strs)
#         for i in range(1, cnt):
#             prefix = self._longestCommonPrefix(prefix, strs[i])
#             if not prefix:
#                 break
#         return prefix

#     def _longestCommonPrefix(self, str1: str, str2: str) -> str:
#         length, idx = min(len(str1), len(str2)), 0
#         while idx < length and str1[idx] == str2[idx]:
#             idx += 1
#         return str1[:idx]


# # 纵向对比 32ms 76%
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         length, cnt = len(strs[0]), len(strs)
#         for i in range(length):
#             ch = strs[0][i]
#             if any(i == len(strs[j]) or strs[j][i] != ch for j in range(1, cnt)):
#                 return strs[0][:i]
#         return strs[0]


# @lc code=end
