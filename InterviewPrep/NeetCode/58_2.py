# Strip trailing whitespaces, iterate from right to left and count till first whitespace is hit 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        modified_s = s.strip()
        
        length = 0
        for i in range(len(modified_s)-1, -1, -1):
            if modified_s[i] == " ":
                break
            
            length += 1

        return length