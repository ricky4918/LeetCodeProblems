class Solution:

    def twoSum(self, nums, target):

        visited = {}

        for index, value in enumerate(nums):

            v1 = target - value
            if v1 in visited:
                return [index, visited[v1]]

            else:
                visited[value] = index

        return False


res = Solution()
nums = [2, 7, 11, 15]
target = 18

print(res.twoSum(nums, target))
