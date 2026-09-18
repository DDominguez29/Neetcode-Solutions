class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       unique = sorted(set(nums))
       nums[0:len(unique)] = unique
       return len(unique)