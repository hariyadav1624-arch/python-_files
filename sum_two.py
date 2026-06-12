class Solution(object):
    def twoSum(self, nums, target):
    
       for i in range(len(nums)):
         for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
               print([i,j])

object=Solution()
nums=list(map(int,input().split()))
target=int(input())
object.twoSum(nums,target)