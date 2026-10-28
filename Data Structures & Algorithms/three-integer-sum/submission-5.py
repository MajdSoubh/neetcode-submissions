class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if (num > 0):
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while (l < r):
                sum = nums[l]+nums[r]+num
                if (sum > 0):
                    r -= 1
                elif (sum < 0):
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l < r):
                        if (nums[l] == nums[l-1]):
                            l += 1
                        else:
                            break

        return result