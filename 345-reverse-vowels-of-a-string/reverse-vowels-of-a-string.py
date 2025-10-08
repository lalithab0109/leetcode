class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow_index=[]
        s=list(s)
        for i in range(0,len(s)):
            if (s[i].lower()) in ['a','e','i','o','u'] :
                vow_index.append(i)
        for i in range(0,(len(vow_index)/2)):
            temp=s[vow_index[i]]
            s[vow_index[i]]=s[vow_index[len(vow_index)-1-i]]
            s[vow_index[len(vow_index)-1-i]]=temp
        #return vow_index
        ans=""
        for i in  range(0,len(s)):
            ans+=s[i]
        return ans
        