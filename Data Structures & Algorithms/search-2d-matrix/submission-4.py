class Solution:

    def find_row_index(self, matrix: List[List[int]], target: int) -> int:
        '''
        Given a matrix and a target, return the index of the row to search,
        or -1 if not in matrix. Uses binary search.
        '''
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            # If target < last value in middle row, search left
            if target < matrix[m][0]:
                r = m - 1
            # If target > last value in middle row, search right
            elif target > matrix[m][-1]:
                l = m + 1
            # Value may be in the middle row
            else:
                return m

        return -1

    def search_row(self, row: List[int], target: int) -> bool:
        '''
        Search for the target value in the row using binary search.
        Return true if found, false otherwise.
        '''
        l = 0
        r = len(row) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                assert row[m] == target
                return True
        
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach:
        # - Binary search to find the row
        # - Then binary search for the value within the row
        i_row = self.find_row_index(matrix, target)
        return self.search_row(matrix[i_row], target)



        