nums=[5,6,7,8,9]
k=2
step = k % len(nums)
nums[:] = nums[-step:]+nums[:-step]
print(nums)

