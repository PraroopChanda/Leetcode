class Trienode:
    def __init__(self):
        self.children={}
        self.endofword=False    

class Trie:

    def __init__(self):
        self.root=Trienode()
        

    def insert(self, word: str) -> None:
        current=self.root

        for c in word:
            if c not in current.children:
                current.children[c]=Trienode()
            current=current.children[c] ## updating the current word
        current.endofword=True ## once i am done with the word i will make end as True

    def search(self, word: str) -> bool:
        current=self.root

        for c in word:
            if c not in current.children:
                return False
            current=current.children[c]
        return current.endofword   ### this will if the word was added or not      
   

    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for c in prefix:
            if c not in current.children:
                return False
            current=current.children[c]
        return True        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)