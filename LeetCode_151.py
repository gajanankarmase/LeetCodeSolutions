class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string 
        splitted_str = s.split()
      
        # reverse the splitted string
        rev_spli_str = splitted_str[::-1]
      
        # place holder to store result
        res = ""
      
        # loop through every word and add space before the word
        for i in rev_spli_str:
            res = res + " " + i
          
        # return res with lstrip() so that the unwanted will get removed
        return res.lstrip()
