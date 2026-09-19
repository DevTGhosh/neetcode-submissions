class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)        
        ans = len(setNums) != len(nums)
        return ans
        