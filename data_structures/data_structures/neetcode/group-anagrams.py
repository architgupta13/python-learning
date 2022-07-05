"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
import collections
from typing import List


class Solution:
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        uniq_dict = dict()

        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item in uniq_dict.keys():
                uniq_dict[sorted_item].append(item)
            else:
                uniq_dict[sorted_item] = [item]

        return [v for v in uniq_dict.values()]

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            s = "".join(sorted(st))
            dic[s].append(st)

        return list(dic.values())
