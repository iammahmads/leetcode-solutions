class Solution(object):
    
    def matrix_print(self, matrix):
        for i in range(26):
            print(matrix[i])

        print()
        print()
    
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        
        def mat_mult(A, B):
            # Multiply two 26x26 matrices
            size = 26
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res
        
        def mat_pow(mat, power):
            size = 26
            # Initialize result as identity matrix
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while power > 0:
                if power % 2 == 1:
                    result = mat_mult(result, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return result
        
        def mat_vec_mult(mat, vec):
            # Multiply 26x26 matrix with 26x1 vector
            res = [0] * 26
            for i in range(26):
                for j in range(26):
                    res[i] = (res[i] + mat[i][j] * vec[j]) % MOD
            return res
        
        # create a matrix for transformations
        transformation_matrix = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                to = (i + j + 1) % 26
                transformation_matrix[to][i] += 1
                
        self.matrix_print(transformation_matrix)
        
        s_matrix = [0] * 26
        for ch in s:
            s_matrix[ord(ch) - ord('a')] += 1
        self.matrix_print(s_matrix)
        
        transformation_matrix_power = mat_pow(transformation_matrix, t)
        self.matrix_print(transformation_matrix_power)     
        
        result =  mat_vec_mult(transformation_matrix_power, s_matrix)
        return sum(result) % MOD   

        
        
        
arr = [6,6,8,1,9,9,10,3,9,4,8,5,2,8,10,2,6,8,2,3,3,7,2,6,4,2]
sol = Solution()
print(sol.lengthAfterTransformations("x", 16, arr))