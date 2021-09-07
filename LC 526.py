class Solution:
    def countArrangement(self, n: int) -> int:
        cnt = 0
        visited = [False]* (n + 1)  #cannot reuse a number 
        def backTrack(n, curr, visited):
            nonlocal cnt        #var belongs only to outer method
            if curr > n:  #if goes beyond n, return curr perm, stop recursion 
                cnt += 1        
                return
            for i in range(1, n + 1): #1-indexed 
                if not visited[i] and (curr % i == 0 or i % curr == 0):
                    visited[i] = True
                    backTrack(n, curr + 1, visited)
                    visited[i] = False
        backTrack(n, 1, visited)
        return cnt
