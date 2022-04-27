class Solution:

    def containsDuplicate1(self, nums):
        nums.sort()
        return any([nums[i] == nums[i+1] for i in range(len(nums)-1)])

    def containsDuplicate2(self, nums):
        

        hashset = set()

        for n in nums:

            if n in hashset:
                return True
            
            else:
                hashset.add(n)
        return False


if __name__ == "__main__":

    nums = [1,2,3,1]
    res = Solution()
    print(res.containsDuplicate2(nums))
