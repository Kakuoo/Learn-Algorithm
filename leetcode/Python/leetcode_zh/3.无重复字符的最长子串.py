#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.05%)
# Likes:    6170
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 3.3M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
# 提示：
#
#
# 0
# s 由英文字母、数字、符号和空格组成
#
#
#

# @lc code=start

# 滑动窗口 56ms， 76%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = curr_len = left = 0
        char_dict = set()
        for i in range(len(s)):
            curr_len += 1
            while s[i] in char_dict:
                char_dict.remove(s[left])
                left += 1
                curr_len -= 1
            
                # if curr_len > max_len:
                #     max_len = curr_len  # 此两句有问题，用下面一句话替代
            max_len = max(max_len , curr_len)
            char_dict.add(s[i])
        return max_len



# 40ms 99%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        right, res = -1, 0

        for i, ch in enumerate(s):
            # 字符ch在字典中,且上次出现的下标大于当前长度的起始下标
            if ch in char_dict and char_dict[ch] > right:
                right = char_dict[ch]
                char_dict[ch] = i
            else:
                char_dict[ch] = i
                res = max(res, i - right)
        return res


# 76ms 32%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = set()
        n = len(s)
        right, res = -1, 0

        for i in range(n):
            if i != 0:
                char_dict.remove(s[i - 1])
            while right + 1 < n and s[right + 1] not in char_dict:
                char_dict.add(s[right + 1])
                right += 1
            res = max(res, right - i + 1)
        return res


# @lc code=end
