class Solution_BruteForce:
    def check_anagrams_in_list(self,word,strs: list[str]) -> list[str]:
        anagrams = []
        anagrams.append(word)
        for w in strs:
            if ''.join(sorted(word)) == ''.join(sorted(w)) and word != w:
                anagrams.append(w)
                
        return anagrams
    def is_word_in_groups(self,word,ga: list[list[str]]) -> bool:
        for a in ga:
            for w in a:
                if word == w:
                    return True
        return False
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams = []
        for i in range(0,len(strs)):
            if not self.is_word_in_groups(strs[i],group_anagrams):
                group_anagrams.append(self.check_anagrams_in_list(strs[i],strs=strs[:]))
            
        return group_anagrams
    
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result_dict = {}
        group_anagrams = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if not sorted_word in result_dict:
                result_dict[sorted_word] = list()
                result_dict[sorted_word].append(word)
            else:
                result_dict[sorted_word].append(word)
        for val in result_dict.values():
            group_anagrams.append(val)
        return group_anagrams
class TestCases:
    tc1 = ["eat","tea","tan","ate","nat","bat"]
    tc1res = [["bat"],["nat","tan"],["ate","eat","tea"]]

def _test():
    tc = TestCases()
    sol = Solution_BruteForce()
    sol2 = Solution()
    print(tc.tc1)
    print(f"Brute Force Output: {sol.groupAnagrams(tc.tc1)}")
    print(f"Brute Force Output: {sol2.groupAnagrams(tc.tc1)}")
    pass

if __name__=='__main__':
    _test()