class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set(nums)
        return len(r) < len(nums)