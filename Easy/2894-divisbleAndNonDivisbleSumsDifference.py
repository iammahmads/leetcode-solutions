class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_by_m = 0
        not_divisible_by_m = 0

        for i in range(1, n+1):
            if i%m != 0:
                not_divisible_by_m += i
            else:
                divisible_by_m += i

        return not_divisible_by_m - divisible_by_m



sol = Solution()
print(sol.differenceOfSums(10, 3))