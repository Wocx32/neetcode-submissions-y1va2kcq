class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                item = stack.pop()
                days = idx - item[0]
                res[item[0]] = days
            
            stack.append((idx, temp))
        
        return res