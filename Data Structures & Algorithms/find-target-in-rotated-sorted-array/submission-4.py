
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums)-1
        while (st < end):
            mid = (st+end)//2
            if (nums[mid] > nums[end]):
                st = mid+1
            else:
                end = mid

        bigger_section = False
        if (target > nums[len(nums)-1] and target >= nums[0]):
            bigger_section = True
        end = max(st-1, 0) if bigger_section else len(nums)-1
        st = 0 if bigger_section else st
        while (st <= end):
            mid = (st+end)//2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] >= target):
                end = mid-1
            else:
                st = mid+1
        return -1

