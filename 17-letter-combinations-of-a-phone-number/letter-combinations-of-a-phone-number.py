class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length=len(digits)
        result=[]
        sol=""
        dict_1={1:[],2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],
        5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],
        9:["w","x","y","z"]}

        def dfs(start,sol):
            if len(sol)==length:
                result.append(sol[:])
                return 

            for elem in range(start,len(digits)):
                for chars in dict_1[int(digits[elem])]:
                    sol+=chars
                    dfs(elem+1,sol)
                    sol=sol[:-1]  
        dfs(0,sol)
        if result==[""]:
            return []
        return result         