class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output={}
        for x in strs:
            if tuple(sorted(x)) in output:
                output[tuple(sorted(x))].append(x)
            else:
                output[tuple(sorted(x))]=[x]
        return list(output.values())            

        