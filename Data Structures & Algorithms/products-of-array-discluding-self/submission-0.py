class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1
        result = []
        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        result = [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                result[i] = 0 if n else prod
            else:
                result[i] = prod//n

        return result