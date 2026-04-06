class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        count_s1 = defaultdict(int)

        for i in s1:
            count_s1[i] += 1
        

        l, r = 0, len(s1)

        while r <= len(s2):
            count_substr = defaultdict(int)
            substr = s2[l:r]
            for i in substr:
                count_substr[i] += 1

            if count_s1 == count_substr:
                return True
        
            l, r = l + 1, r + 1

        return False