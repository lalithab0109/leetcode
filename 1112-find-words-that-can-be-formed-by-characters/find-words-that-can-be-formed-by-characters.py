class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_list=list(chars)
        chars_list_org=chars_list
        check=1
        ans=0
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if(words[i][j] in chars_list):
                    chars_list.remove((words[i][j]))
                else:
                    check=0
                    break
            if(check==1):
                ans+=len(words[i])
            chars_list=list(chars)
            check=1
        return ans


        