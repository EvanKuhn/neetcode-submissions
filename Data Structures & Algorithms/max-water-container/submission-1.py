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
        print(f"n={n}")
        a = 0
        b = n-1

        # Save the pointer values (a,b) that yield the highest volume thus far
        best_a = a
        best_b = b
        best_vol = self.calc_volume(heights, best_a, best_b)
        print(f"Init best: h[{a}]={heights[a]}, h[{b}]={heights[b]}, vol={best_vol}")

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










    # def maxArea(self, heights: List[int]) -> int:
    #     # Let's try this:
    #     # - Start with two indexes: one left, one right
    #     # - For the left index, search leftward for the next index with a higher value
    #     # - Likewise for the right index, search leftward for the next index with higher value
    #     # - Compare volumes using:
    #     #   - old_left * old_right
    #     #   - new_left * old_right
    #     #   - old_left * new_right
    #     #   - new_left * new_right
    #     #
    #     # - Keep iterating until indexes cross or we don't find an increase
    #     #
    #     # Return the maximum amount of water that can be stored

    #     n = len(heights)
    #     print(f"n={n}")

    #     a_index = 0
    #     a_value = heights[a_index]

    #     b_index = n-1
    #     b_value = heights[b_index]
        
    #     best_a = a_index
    #     best_b = b_index
    #     best_vol = self.calc_volume(heights, best_a, best_b)
    #     print(f"Init best: h[{a_index}]={a_value}, h[{b_index}]={b_value}, vol={best_vol}")

    #     while(True):
    #         updated = False
    #         a_index_new, a_value_new = self.search_right(heights, a_index)
    #         b_index_new, b_value_new = self.search_left(heights, b_index)

    #         # print(f"Next A: index={a_index_new} value={a_value_new}")
    #         # print(f"Next B: index={b_index_new} value={b_value_new}")

    #         # a_old, b_new
    #         temp_vol = self.calc_volume(heights, a_index_new, b_index)
    #         if temp_vol > best_vol:
    #             best_a = a_index_new
    #             best_b = b_index
    #             best_vol = temp_vol
    #             updated = True
    #             print(f"New best: h[{best_a}]={heights[best_a]}, h[{best_b}]={heights[best_b]}, vol={best_vol}")

    #         # a_new, b_old
    #         temp_vol = self.calc_volume(heights, a_index, b_index_new)
    #         if temp_vol > best_vol:
    #             best_a = a_index
    #             best_b = b_index_new
    #             best_vol = temp_vol
    #             updated = True
    #             print(f"New best: h[{best_a}]={heights[best_a]}, h[{best_b}]={heights[best_b]}, vol={best_vol}")

    #         # a_new, b_new
    #         temp_vol = self.calc_volume(heights, a_index_new, b_index_new)
    #         if temp_vol > best_vol:
    #             best_a = a_index_new
    #             best_b = b_index_new
    #             best_vol = temp_vol
    #             updated = True
    #             print(f"New best: h[{best_a}]={heights[best_a]}, h[{best_b}]={heights[best_b]}, vol={best_vol}")

    #         # If we didn't find a better solution, quit
    #         # - Note, calc_volume will return a NEGATIVE number when indexes cross,
    #         #   
    #         if not updated:
    #             break

            

    #     return best_vol
