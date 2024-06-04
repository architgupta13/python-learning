class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(min([len(str) for str in strs])):
            index = 1
            first = strs[0]
            
            while index < len(strs):
                if strs[index][i] != first[i]:
                    return prefix
                index += 1

            prefix += first[i]

        return prefix 