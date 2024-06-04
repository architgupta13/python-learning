# Iterate from right to left till a non-space character is hit and then start counting

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, found = 0, False

        for i in range(len(s)-1, -1, -1):
            if found and s[i] == ' ':
                break
            
            if s[i] == ' ':
                continue
            
            found = True
            length += 1

        return length