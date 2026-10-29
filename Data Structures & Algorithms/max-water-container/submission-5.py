class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calc_area(heights: List[int], i: int, j: int) -> int:
            return (j - i) * min(heights[i], heights[j])

        # Initialize indexes
        i = 0
        j = len(heights) - 1
        max_area = calc_area(heights, i, j)

        # Move indexes inward
        while j - i > 1:
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

            area = calc_area(heights, i, j)
            if area > max_area:
                max_area = area
        
        return max_area
