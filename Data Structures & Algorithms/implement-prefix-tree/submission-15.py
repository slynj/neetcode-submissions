class PrefixTree:

    def __init__(self):
        # {'l': PrefixTree, -> {'y': PrefixTree} -> {'n': PrefixTree} (self.isEnd = True)
        #  'j': PrefixTree}
        self.children = {}
        self.isEnd = False
        

    def insert(self, word: str) -> None:
        # node = self.
        childrenNode = self.children
        for i in range(len(word)):
            c = word[i]
            if c in childrenNode:
                if i == len(word) - 1:
                    childrenNode[c].isEnd = True
                    return
                else:
                    childrenNode = childrenNode[c].children
            else:
                childrenNode[c] = PrefixTree()
                
                if i == len(word) - 1:
                    childrenNode[c].isEnd = True
                    return
                childrenNode = childrenNode[c].children



    def search(self, word: str) -> bool:
        trie = self.children
        for i in range(len(word)):
            c = word[i]
            if c not in trie:
                return False
            if i == len(word) - 1:
                return trie[c].isEnd == True
            trie = trie[c].children


    def startsWith(self, prefix: str) -> bool:
        trie = self.children
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in trie:
                return False
            trie = trie[c].children
        return True
        
        