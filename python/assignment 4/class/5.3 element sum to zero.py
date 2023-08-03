# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers. 
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 

from itertools import combinations
class ThreeSumFinder:
    def three_sum_zero(self, nums):
        return [[x, y, z] for x, y, z in combinations(nums, 3) if x + y + z == 0]
input_array = [-25, -10, -7, -3, 2, 4, 8, 10]
sum_finder = ThreeSumFinder()
output = sum_finder.three_sum_zero(input_array)
print(output)

