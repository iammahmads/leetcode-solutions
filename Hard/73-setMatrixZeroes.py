from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows_with_zero = set()
        cols_with_zero = set()
        
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)
        
        for row in rows_with_zero:
            for col in range(m):
                matrix[row][col] = 0
                
        for col in cols_with_zero:
            for row in range(n):
                matrix[row][col] = 0

        # print(matrix)
        
sol = Solution()
sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
                    