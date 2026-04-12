class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for idx in range(len(temperatures)):

            while stack and temperatures[idx] > temperatures[stack[-1]]:

                popped = stack.pop()

                res[popped] = idx - popped
        
            stack.append(idx)

        return res