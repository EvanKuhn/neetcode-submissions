from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get frequencies
        num_freq_map = defaultdict(int)
        for n in nums:
            num_freq_map[n] += 1

        # Get list of (value, freq) tuples sorted by freq, descending
        freqs_desc = list(num_freq_map.items())
        freqs_desc.sort(key=lambda x: x[1], reverse=True)

        # Return top k
        return [x[0] for x in freqs_desc[0:k]]
