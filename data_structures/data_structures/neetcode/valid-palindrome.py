"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.



Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ""
        s = s.lower()
        for i in range(len(s)):
            if 97 <= ord(s[i]) <= 122 or s[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                formatted_s += s[i]

        i = 0
        j = len(formatted_s) - 1

        while i < len(formatted_s) // 2:
            if formatted_s[i] != formatted_s[j]:
                return False

            i += 1
            j -= 1

        return True
