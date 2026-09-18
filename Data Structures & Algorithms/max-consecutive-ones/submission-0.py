class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for ones in nums:
            if ones == 1:
                count += 1
                if max <= count:
                    max = count
            elif ones == 0:
                count = 0
        return max
        