from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for f in range(len(nums)):
           

            required_pair = target - nums[f]
            if required_pair in map:
                return [ map[required_pair], f]
            map[nums[f]] = f
        return []

