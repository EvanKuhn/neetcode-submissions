# Possible ranges of k:
#
#     If:               Then:
#     k = 1             h = sum(piles)
#     k = max(piles)    h = len(piles)
#
# We can do this in a binary search:
# - Start with k_min=1, k_max=max(piles)
# - while k_min <= k_max:
#   - Compute k_mid = value between k_min and k_max
#   - Recompute total hours by summing hours per pile:
#     - hours = math.ceil(pile[i] / k_mid
#   - Move k_min or k_max to k_mid

class Solution:
    def compute_hours(self, piles: List[int], k: int) -> int:
        '''
        Given the array of banana piles, and an integer k of bananas/hour,
        compute and return the total time to eat all of the piles.
        '''
        return sum([math.ceil(p / k) for p in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Return the minimum integer k such that you can eat all the bananas 
        within h hours.
        '''
        k_min = 1
        k_min_hrs = sum(piles)
        
        k_max = max(piles)
        k_max_hrs = len(piles)

        print(f"k_min={k_min}, hours={k_min_hrs}")
        print(f"k_max={k_max}, hours={k_max_hrs}")
        
        while k_min < k_max:
            k_mid = k_min + ((k_max - k_min) // 2)
            k_mid_hrs = self.compute_hours(piles, k_mid)
            print(f"- k_mid={k_mid}, hours={k_mid_hrs}")

            # If the middle is too slow, search to the right (higher banana-eating rate)
            # Else, search the left (lower rate, which we want)
            if k_mid_hrs > h:
                k_min = k_mid
                k_min_hrs = k_mid_hrs
            else:
                k_max = k_mid
                k_max_hrs = k_mid_hrs

            print(f"k_min={k_min}, hours={k_min_hrs}")
            print(f"k_max={k_max}, hours={k_max_hrs}")


            # Stopping point: k_min and k_max are 1 apart
            if k_max - k_min == 1:
                print("stopping here")
                if k_min_hrs <= h:
                    return k_min
                if k_max_hrs <= h:
                    return k_max
                return -1
        
        return k_min
            

        