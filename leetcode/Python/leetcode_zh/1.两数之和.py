#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (52.02%)
# Likes:    12209
# Dislikes: 0
# Total Accepted:    2.5M
# Total Submissions: 4.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#
# 示例 3：
#
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
#
#
# 提示：
#
#
# 2
# -10^9
# -10^9
# 只会存在一个有效答案
#
#
# 进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
#
#

# @lc code=start

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if target - nums[idx] in hashmap:
                return [idx, hashmap.get(target - nums[idx])]
            else:
                hashmap[num] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if hashmap.get(target - nums[idx]) is not None:
                return [idx, hashmap.get(target - nums[idx])]
            hashmap[num] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp_nums = nums[:i]    # 每轮只搜索比对[0, i]的元素内容
            if (target - nums[i]) in temp_nums:
                j = temp_nums.index(target - nums[i])
                break
        if j >= 0:
            return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                    continue
                else:
                    j = nums.index(target - nums[i], i + 1)
                    break
        if j > 0:
            return [i, j]
        else:
            return []


# @lc code=end
