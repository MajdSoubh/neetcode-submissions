class Solution:
    def findMin(self, nums: List[int]) -> int:
        st = 0
        end = len(nums)-1
        while (st != end):
            mid = (st+end)//2
            if (nums[mid] <= nums[end]):
                end = mid
            else:
                st = mid+1
        return nums[st]