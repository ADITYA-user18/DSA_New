nums = [2, 1, 5, 1, 3, 2]
k = 3

curr = 0
maxi = 0

# First window
for i in range(k):
    curr += nums[i]

maxi = curr

# Slide the window
for i in range(k, len(nums)):
    curr += nums[i] - nums[i-k]

    if curr > maxi:
        maxi = curr

print(maxi)
