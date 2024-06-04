# Use character array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_counts = [0] * 26

        for ch in s:
            alpha_counts[ord(ch) - ord('a')] += 1

        for ch in t:
            alpha_counts[ord(ch) - ord('a')] -= 1

        for count in alpha_counts:
            if count != 0:
                return False

        return True