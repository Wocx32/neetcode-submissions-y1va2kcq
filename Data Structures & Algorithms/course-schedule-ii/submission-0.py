class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        taken = 0
        res_path = []
        while q:
            # print(q)

            course = q.popleft()
            res_path.append(course)
            taken += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if taken != numCourses:
            return []
        return res_path