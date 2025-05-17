class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # def merge_sort(nums_list):
        #     n = len(nums_list)
        #     if n <= 1:
        #         return nums_list
            
        #     middle = n // 2
        #     left = merge_sort(nums_list[:middle])
        #     right = merge_sort(nums_list[middle:])
        #     # print("right: ", right)
            
        #     return merge(left, right)
            
        # def merge(left, right):
        #     result = list()
        #     i = j = 0
            
        #     left_len, right_len = len(left), len(right)
        #     while i < left_len and j < right_len:
        #         if left[i] <= right[j]:
        #             result.append(left[i])
        #             i += 1
        #         else:
        #             result.append(right[j])
        #             j += 1
        #     # extend any remaining elements in left or right
        #     while i < left_len:
        #         result.append(left[i])
        #         i += 1
        #     while j < right_len:
        #         result.append(right[j])
        #         j += 1
        #     return result  
             
        
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        return bubble_sort(nums)


        
sol = Solution()
print(sol.sortColors([2,0,2,1,1,0]))