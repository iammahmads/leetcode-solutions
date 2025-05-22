from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        
    def longest_commom_prefix(self) -> str:
        prefix = ""
        node = self.root
        
        while node:
            if len(node.children) != 1 or node.is_end:
                break
            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]
        return prefix
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            trie.insert(word)
            
        return trie.longest_commom_prefix()
    
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))