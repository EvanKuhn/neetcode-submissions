# Thoughts
# - Establish right and left bounds:
#   - min_i = search from left until the next height is smaller
#   - max_i = search from right until the 'next' height is smaller
#   - This establishes your right and left bounds
# - Now start at i = j = min_i:
#   - increment j until you find height[j] >= height[i]
#     - calculate rainwater volume between i and j
#   - move j until height at j+1 is lower
#   - set i = j

class Solution:
    def find_min_i(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        while i < n-1 and height[i+1] >= height[i]:
            i += 1
        return i

    def find_max_i(self, height: List[int]) -> int:
        i = len(height) - 1
        while i > 0 and height[i-1] >= height[i]:
            i -= 1
        return i

    def calc_volume(self, height: List[int], i: int, j: int) -> int:
        volume = 0
        min_height = min(height[i], height[j])
        # print(f"calc_volume({i}, {j})")
        for x in range(i+1, j):
            volume += max(0, min_height - height[x])
        # print(f"volume between {i} and {j} is {volume}")
        return volume

    def trap(self, height: List[int]) -> int:
        min_i = self.find_min_i(height)
        max_i = self.find_max_i(height)
        if len(height) < 100:
            print(height)
        else:
            print(height[0:50])
            print("...")
            print(height[-50:])
        print("len(height) =", len(height))
        print(f"min_i = {min_i}")
        print(f"max_i = {max_i}")


        i = min_i
        volume = 0

        # print(height)

        while i < max_i-1:
            # Increment j until height_j >= height_i
            j = i+2 # Incr by 2 to leave space for water

            # - Save for special case at end:
            max_height = height[j]
            max_height_index = j

            while j < max_i and height[j] < height[i]:
                cur_height = height[j]
                if cur_height > max_height:
                    max_height = cur_height
                    max_height_index = j
                j += 1

            # Special case: if we hit max_i, we really want to back up
            # to the highest wall between i and max_i
            if j == max_i:
                if max_height > height[j]:
                    j = max_height_index
            
            # We found the next wall. Calculate volume.
            volume += self.calc_volume(height, i, j)

            # Now move j until the height[j+1] is smaller
            while j < max_i and height[j+1] >= height[j]:
                j += 1

            # Now move i to j and iterate
            i = j

        return volume



        