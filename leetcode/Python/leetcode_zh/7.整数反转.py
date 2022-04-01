#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (35.29%)
# Likes:    3167
# Dislikes: 0
# Total Accepted:    858.5K
# Total Submissions: 2.4M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
#
#
# 示例 1：
#
#
# 输入：x = 123
# 输出：321
#
#
# 示例 2：
#
#
# 输入：x = -123
# 输出：-321
#
#
# 示例 3：
#
#
# 输入：x = 120
# 输出：21
#
#
# 示例 4：
#
#
# 输入：x = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#

# @lc code=start


# 28ms 92% 调整代码顺序，提升判断返回的速度
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        while x:
            digit = x % 10
            # Python3的取模运算在x为负数时也会返回 [0, 9) 以内的结果，
            # 因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10
             # 同理Python3的整数除法在x为负数时会向下（更小的负数）取整，
             # 因此不能写成 x //= 10
            x = (x - digit) // 10
            res = res * 10 + digit

            if res < INT_MIN or res > INT_MAX:
                return 0
        return res


# 40ms 26%
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        while x:
            digit = x % 10
            # Python3的取模运算在x为负数时也会返回 [0, 9) 以内的结果，
            # 因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10
             # 同理Python3的整数除法在x为负数时会向下（更小的负数）取整，
             # 因此不能写成 x //= 10
            x = (x - digit) // 10
            res = res * 10 + digit

            if res < INT_MIN or res > INT_MAX:
                return 0
        return res


# 傻逼解法 44ms 9.5%
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            s = str(x)
            s = s[::-1]
            x = int(s)
        else:
            s = str(x)
            s = s[1:]
            s = s[::-1]
            x = int("-" + s)

        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x

# @lc code=end
