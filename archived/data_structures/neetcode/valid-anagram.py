"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.



Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

import collections


class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) != len(sorted_t):
            return False

        for idx, item in enumerate(sorted_s):
            if item != sorted_t[idx]:
                return False

        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        counts = dict()

        for item in s:
            if item not in counts.keys():
                counts[item] = 1
            else:
                counts[item] += 1

        for item in t:
            if item not in counts.keys():
                return False

            counts[item] -= 1

        for k, v in counts.items():
            if v != 0:
                return False

        return True

    def isAnagram_3(self, s: str, t: str) -> bool:
        counts = [0 for i in range(26)]

        for item in s:
            counts[ord(item) - ord("a")] += 1

        for item in t:
            counts[ord(item) - ord("a")] -= 1

        return True if all([cnt == 0 for cnt in counts]) else False

    def isAnagram_4(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
