class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_len=len(beginWord)    
        #nei=collections.defaultdict(list)
        nei=dict()
        wordList.append(beginWord)
        for word in wordList:
            for j in range(word_len): ## iterating through each letter
                pattern=word[:j]+"*"+word[j+1:]
                if pattern in nei:
                    nei[pattern].append(word)
                else:
                    nei[pattern]=[word]

        ## done creating the adjacency list --> now starting with BFS
        visited=set([beginWord])
        q=deque([beginWord])
        res=1

        #print(nei)
        ## going for a BFS
        while q:
            for i in range(len(q)): ## processing all adjacent once then incrementing
                word=q.popleft()
                if word==endWord:
                    return res   
                for j in range(word_len):
                    pattern=word[:j]+"*"+word[j+1:]
                    for words in nei[pattern]:
                        if words not in visited: ## highly important don't visit same node twice
                            visited.add(words)
                            q.append(words)
            res+=1                    

        return 0

                        



             
        