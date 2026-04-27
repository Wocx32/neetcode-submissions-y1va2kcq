class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for word in words:
            trie.insert_word(word)
        
        visit = set()
        res = set()

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, currWord):

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            currWord += board[r][c]

            if node.endOfWord:
                res.add(currWord)

            dfs(r + 1, c, node, currWord)
            dfs(r - 1, c, node, currWord)
            dfs(r, c + 1, node, currWord)
            dfs(r, c - 1, node, currWord)

            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        
        return list(res)