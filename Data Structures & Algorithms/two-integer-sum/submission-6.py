
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(v, i) for i, v in enumerate(nums)]
        nums = sorted(nums, key=lambda item: item[0])
        i = 0
        j = len(nums)-1
        while (i != j):
            if nums[j][0] + nums[i][0] > target:
                j -= 1

            elif nums[j][0] + nums[i][0] < target:
                i += 1
            elif nums[j][0] + nums[i][0] == target:
                lower_index = min(nums[j][1], nums[i][1])
                max_index = max(nums[j][1], nums[i][1])
                return [lower_index, max_index]
        return []
