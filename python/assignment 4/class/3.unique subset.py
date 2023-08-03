class SubsetGenerator:

    def subsets(self, nums):
        self.result = []
        self._generate_subsets(nums, 0, [])
        return self.result

    def _generate_subsets(self, nums, index, current_subset):
        # Add the current subset to the result list
        self.result.append(current_subset[:])

        # Generate subsets by adding each element to the current subset
        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            self._generate_subsets(nums, i + 1, current_subset)
            current_subset.pop()

if __name__ == "__main__":
    nums = [4, 5, 6]
    generator = SubsetGenerator()
    subsets = generator.subsets(nums)
    print(subsets)
