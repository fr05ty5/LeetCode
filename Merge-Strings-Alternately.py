class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        s = []
        while i< min(len(word1),len(word2)):
            s.append(word1[i])
            s.append(word2[i])
            i+=1
        
        if len(word1) > len(word2):
            s.append(word1[-(len(word1)-len(word2)):])
        elif len(word2) > len(word1):
            s.append(word2[-(len(word2)-len(word1)):])
        
        return ''.join(s)