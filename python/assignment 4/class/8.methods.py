# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order 
class StringProcessor:

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        if hasattr(self, 'input_string'):
            print("Reversed string:", self.input_string[::-1])
        else:
            print("No input string. Please call get_string() first.")

if __name__ == "__main__":
    processor = StringProcessor()
    processor.get_string()
    processor.print_string()


