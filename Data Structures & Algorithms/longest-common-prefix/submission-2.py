class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]
    
    def lcp(self, word, prefix_len):
        node = self.root
        for i in range(min(len(word), prefix_len)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        
        return min(len(word), prefix_len)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        mini = 0

        for i in range(len(strs)):
            if len(strs[i]) < len(strs[mini]):
                mini = i
        
        trie = Trie()
        trie.insert(strs[mini])
        prefix_len = len(strs[mini])
        for i in range(len(strs)):
            prefix_len = trie.lcp(strs[i], prefix_len)
        return strs[0][:prefix_len]       