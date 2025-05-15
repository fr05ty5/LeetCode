class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        string = ""
        while i< min(len(word1),len(word2)):
            string = string+word1[i]+word2[i]
            i+=1
        
        
        if len(word1) > len(word2):
            string = string + word1[-(len(word1)-len(word2)):]
        elif len(word2) > len(word1):
            string = string + word2[-(len(word2)-len(word1)):]
        return string