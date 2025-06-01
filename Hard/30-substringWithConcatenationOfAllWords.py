from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        n = len(s)
        result = []

        for i in range(n - total_len + 1):
            seen = {}
            for j in range(0, total_len, word_len):
                word = s[i + j:i + j + word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
            else:
                result.append(i)

        return result



sol = Solution()
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))