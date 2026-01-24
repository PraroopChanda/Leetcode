class trienode:
    def __init__(self):
        self.children={}
        self.endofWord=False

class WordDictionary:

    def __init__(self):
        self.root=trienode()

    def addWord(self, word: str) -> None:
        current=self.root
        for w in word:
            if w not in current.children:
                current.children[w]=trienode()
            current=current.children[w]     
        current.endofWord=True
                
    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i ==len(word):
                return node.endofWord

            w=word[i]

            if w!=".":
                if w not in node.children:
                    return False
                return dfs(i+1,node.children[w])

            else:
                for child in node.children.values():
                    if dfs(i+1,child): ## because there can be some words, which are not the end of word but some are
                        return True ## basically doing it for all nodes skipping one in between, because using values
            return False
        return dfs(0,self.root)            






        # current=self.root
        # for w in word:
        #     if w not in current.children and w!=".":
        #         return False
        #     if w!=".":
        #         current=current.children[w]  
        #     else: ## basically choosing all nodes whose parent is previous word
        #         new_chain=trienode()
        #         for keys in current.children: ## car, cut, cute--> [a,t]
        #             for key in current.children[keys].children: ## 
        #                 new_chain.children[key]=current.children[keys].children[key] 
        #         current=new_chain       
        # return current.endofWord      
        # return False        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)