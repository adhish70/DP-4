# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

# Logic: Each cell is 1 + min of its 3 neighbours before it only if current node is 1.

# Time Complexity: O(nm)
# Space Complexity: O(nm)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0 for i in range(m)] for j in range(n)]
        max_area = 0
        
        # Initialize first row with input
        for j in range(m):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                max_area = max(max_area, dp[0][j])
            else:
                dp[0][j] = 0
        
        # Initialize first col with input
        for i in range(n):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_area = max(max_area, dp[i][0])
            else:
                dp[i][0] = 0
        
        # Fill dp
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_area = max(max_area, dp[i][j])
        
        return max_area*max_area