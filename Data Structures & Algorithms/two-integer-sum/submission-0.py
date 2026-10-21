class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for f in range(len(nums)-1):
            for s in range(f+1, len(nums)):
                if nums[f] + nums[s] == target:
                    return [f, s]

        return []
