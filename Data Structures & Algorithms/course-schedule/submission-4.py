class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        
        q = deque()
        completed = 0

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(course)
        
        while q:
            course = q.pop()

            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

            completed += 1
        
        return completed == numCourses