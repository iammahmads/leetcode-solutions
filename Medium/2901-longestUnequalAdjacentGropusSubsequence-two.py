class Solution:
  def getWordsInLongestSubsequence(
      self,
      words,
      groups,
  ):
    n = len(words)
    # dp[i] := the length of the longest subsequence ending in `words[i]`
    result = [1] * n
    # prev[i] := the best index of words[i]
    prev = [-1] * n

    ans = []
    for i in range(1, n):
      for j in range(i):
        if groups[i] == groups[j]:
          continue
        if len(words[i]) != len(words[j]):
          continue
        if sum(a != b for a, b in zip(words[i], words[j])) != 1:
          continue
        if result[i] < result[j] + 1:
          result[i] = result[j] + 1
          prev[i] = j

    # Find the last index of the subsequence.
    index = result.index(max(result))
    while index != -1:
      ans.append(words[index])
      index = prev[index]

    return ans[::-1]

        
        
sol = Solution()
print(sol.getWordsInLongestSubsequence(["bdb","aaa","ada"], [1, 2, 3]))