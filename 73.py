nums=[3,2,4]
target=6
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==target-nums[j]:
            a=[i,j]
            print(a)
            print(nums[i],nums[j])
