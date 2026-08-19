class Solution:
    def search_right(self, heights: List[int], index: int) -> tuple[int,int]:
        '''
        Given the heights array and a starting index, search rightward for the
        next index with value greater than the one at heights[index].
        - Return (None, None) if not found
        '''
        cur_height = heights[index]
        for i in range(index+1, len(heights)):
            if(heights[i]) > cur_height:
                return i, heights[i]
        return None, None

    def search_left(self, heights: List[int], index: int) -> tuple[int,int]:
        '''
        Given the heights array and a starting index, search leftward for the
        next index with value greater than the one at heights[index].
        - Return (None, None) if not found
        '''
        cur_height = heights[index]
        for i in range(index-1, -1, -1):
            if(heights[i]) > cur_height:
                return i, heights[i]
        return None, None

    def calc_volume(self, heights: List[int], a: int, b: int) -> int:
        '''
        Calculate volume given heights and two indexes.
        '''
        return (b - a) * min(heights[a], heights[b])

    def maxArea(self, heights: List[int]) -> int:
        # Initialize indexes a,b
        n = len(heights)
        #print(f"n={n}")
        a = 0
        b = n-1

        # Save the pointer values (a,b) that yield the highest volume thus far
        best_a = a
        best_b = b
        best_vol = self.calc_volume(heights, best_a, best_b)
        #print(f"Init best: h[{a}]={heights[a]}, h[{b}]={heights[b]}, vol={best_vol}")

        while(True):
            # Move the shorter pointer
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
            
            # Quit if pointers cross
            if a >= b:
                break

            # Calculate new volume. Store it if it is better.
            temp_vol = self.calc_volume(heights, a, b)
            if temp_vol > best_vol:
                best_a = a
                best_b = b
                best_vol = temp_vol

        return best_vol
