class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[n-1] = 1
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        return [left[i]*right[i] for i in range(n)]
