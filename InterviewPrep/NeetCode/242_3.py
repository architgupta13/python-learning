# Use 1 hashmap and update counts in iteration

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = {}

        for ch in s:
            char_counts[ch] = char_counts.get(ch, 0) + 1

        for ch in t:
            if ch not in char_counts:
                return False

            char_counts[ch] -= 1

        for v in char_counts.values():
            if v != 0:
                return False

        return True