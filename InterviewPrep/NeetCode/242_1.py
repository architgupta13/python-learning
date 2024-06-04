# Use 2 hashmaps for respective counts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_uniqs_count, t_uniqs_count = {}, {}
        for ch in s:
            s_uniqs_count[ch] = s_uniqs_count.get(ch, 0) + 1
        
        for ch in t:
            t_uniqs_count[ch] = t_uniqs_count.get(ch, 0) + 1

        for k, v in s_uniqs_count.items():
            if k not in t_uniqs_count.keys():
                return False
            
            t_uniqs_count[k] -= v
        
        for value in t_uniqs_count.values():
            if value != 0:
                return False
        
        return True
