def areAnagrams():
   word1, word2 = input().split(" ")

   if len(word1) != len(word2):
       return 0

    return sorted(word1) == sorted(word2)
   
    

    
