nums = [2, 1, 5, 2, 3, 2]
target = 7


def min_targeter(nums,target):
    left = 0
    sums = 0 
    minimer = float('inf')

    for right in range(0,len(nums)):

        sums += nums[right]
        
        while sums >= target:
            minimer  = min(minimer,right-left+1)
            sums-=nums[left]
            left+=1





    return minimer



print(min_targeter(nums,target))










