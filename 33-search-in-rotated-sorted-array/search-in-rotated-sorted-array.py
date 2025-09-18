class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## The logic is basically to always choose a correct side to search and then the middle one would be the target
        left,right=0,len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1                            
