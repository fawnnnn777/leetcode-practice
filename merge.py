class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        len1 = len(word1)
        len2 = len(word2)
        if len1 > len2:
            for i in range(len1):
                print(word1[i])
                word += word1[i]
                if i > len2 or i == len2:
                    i+=1
                else:
                    print(word2[i])
                    word += word2[i]
        else:
            for i in range(len2):
                if i < len1 or i == len1-1:
                    print(word1[i])
                    word +=word1[i]
                print(word2[i])
                word += word2[i]
        return word

