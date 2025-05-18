class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        MOD = 1000000007
        dp_result = [[0]* (1 << (2*m)) for _ in range(n+1)]
        
        def dp(row, col, prevColumn, currentColumn):
            if col == n:
                return 1
            if row == m:
                return dp(0, col+1, currentColumn, 0)
            if row == 0 and dp_result[col][prevColumn]:
                return dp_result[col][prevColumn]
            
            total = 0
            upper_row_colored = (currentColumn >> ((row - 1) * 2) & 3) if row > 0 else 0
            left_col_colored = (prevColumn >> (row*2)) & 3
            # print("upper_row_colored: ", upper_row_colored)
            # print("left_col_colored: ", left_col_colored)
            # print()
            for i in range(1, 4):
                if i != upper_row_colored and i != left_col_colored:
                    total = ( total + dp(row+1, col, prevColumn, currentColumn + (i << (row * 2)))) % MOD
            
            total = total % MOD
            if row == 0:
                dp_result[col][prevColumn] = total
            return total
        
        return dp(0, 0 ,0, 0)
                
        
                
        
sol = Solution()
print(sol.colorTheGrid(3, 3))