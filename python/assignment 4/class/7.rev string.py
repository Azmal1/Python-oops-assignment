# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 
class StringReverse:
    def reverse_words(self,input_string):
        words=input_string.split()
        reversed_words=words[::-1]
        output_string=" ".join(reversed_words)
        return output_string
if __name__=="__main__":
    rev=StringReverse()
    input_string="hello .py"
    res=rev.reverse_words(input_string)
    print(input_string)
    print(res)
