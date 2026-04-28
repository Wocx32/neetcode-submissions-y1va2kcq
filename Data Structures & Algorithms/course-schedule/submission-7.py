class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()

        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)
        
        done = 0
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                for nei in adj[course]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                done += 1
        
        return done == numCourses