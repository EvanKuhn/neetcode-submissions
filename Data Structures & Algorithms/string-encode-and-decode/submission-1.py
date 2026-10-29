
class Solution:

    def encode(self, strs: List[str]) -> str:
        len_str_pairs = [f"[{len(s)}]{s}" for s in strs]
        return "".join(len_str_pairs)
        

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            # Remove '['
            assert s[0] == '['
            s = s[1:]

            # Read the next string's length and value
            lenstr, s = s.split(']', 1)
            length = int(lenstr)
            token = s[:length]
            s = s[length:]
            strs.append(token)

        return strs
        

