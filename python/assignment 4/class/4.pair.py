
# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 

class TwoSumFinder:

    def find_two_sum_indices(self, numbers, target):
        seen = {}  # Dictionary to store elements and their corresponding indices

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return seen[complement], i
            seen[num] = i

        return None  # If no valid pair is found, return None

if __name__ == "__main__":
    numbers = [90, 20, 10, 40, 50, 60, 70]
    target = 50

    finder = TwoSumFinder()
    result = finder.find_two_sum_indices(numbers, target)

    if result is not None:
        index1, index2 = result
        print(f"Output: {index1}, {index2}")
    else:
        print("No pair found.")
