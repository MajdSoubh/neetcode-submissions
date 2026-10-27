class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_result = 0
        while (l < r):
            size = (r-l)*(min(heights[l], heights[r]))
            max_result = max(max_result, size)
            if (heights[l] <= heights[r]):
                l += 1
            elif (heights[l] > heights[r]):
                r -= 1
        return max_result