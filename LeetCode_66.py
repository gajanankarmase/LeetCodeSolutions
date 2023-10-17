class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""
        for i in digits:
            num_str += str(i)
        
        num = int(num_str) + 1
        
        output_arr = []
        
        for j in str(num):
            output_arr.append(int(j))    
        return output_arr
