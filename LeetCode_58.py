class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # splitted the original string
        splitted_str = s.split()
        # saved the last word index
        last_word_index = len(splitted_str) - 1
        # saved the last word
        last_word = splitted_str[last_word_index]
        # created an empty list to store the splitted last word
        last_word_list = []
        # Looped through the last word and appended it to the above list
        for i in last_word:
            last_word_list.append(i)
        # returned the lenght of the splitted last word
        return len(last_word_list)
