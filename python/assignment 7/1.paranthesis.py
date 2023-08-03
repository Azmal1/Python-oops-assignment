# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

def is_balanced_delimiters(input_str):
    stack = []
    opening_chars = "({["
    closing_chars = ")}]"

    for char in input_str:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack:
                return False
            last_opening_char = stack.pop()
            if opening_chars.index(last_opening_char) != closing_chars.index(char):
                return False

    return len(stack) == 0

if __name__ == "__main__":
    input_str = "([{}])"
    result = is_balanced_delimiters(input_str)
    print(result)  # Output: True
