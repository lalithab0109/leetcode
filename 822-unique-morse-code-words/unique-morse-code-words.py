class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s=""
        l=[]
        alpha_morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        aplha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if words[i][j] in aplha:
                    k=aplha.index(words[i][j])
                    s=s+alpha_morse[k]
            l.append(s)
            s=""
        ls=set(l)
        return len(ls)


