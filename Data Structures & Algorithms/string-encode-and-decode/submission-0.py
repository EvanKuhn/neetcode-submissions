
def read_length(s: str, i: int) -> tuple(int, int):
    '''
    Takes a string 's' and index 'i'. The string is formatted as:

        [<len>]<chars>[<len>]<chars>...

    Index 'i' is expected to point to one of the [<len>] values, which
    this function will read and parse. 
    
    Returns a tuple of (i, length), where:
    
        i      = Index of next char after the "[<len>]" substring
        length = Value denoted in the [<len>] substr we just parsed.

    '''
    #print(f"Called read_length() on '{s[i:10]}'...")
    assert s[i] == "["
    lenstr = ""
    while True:
        i += 1
        if s[i] == "]":
            i += 1
            break
        assert '0' <= s[i] <= '9', f"{s[i]} is not between 0 and 9"
        lenstr += s[i]
    #print(f"Returning ({i},{int(lenstr)})")
    return (i, int(lenstr))


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Prepend "[len]" to the strings, and concatenate all of these
        len_strs = [f"[{len(s)}]{s}" for s in strs]
        return "".join(len_strs)

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        # Read each string by first reading the length N, then getting the 
        # actual string (next N chars)
        while i < len(s):
            i, length = read_length(s, i)
            results.append(s[i:i+length])
            i += length
        return results


