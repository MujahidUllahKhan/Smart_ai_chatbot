def arr(nums,target):
    result=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
               result.append((i,j))
    return result
ac=arr([1,2,3,4,5],7)
ab=(nums,target)
for i , j in (ab):
 print("The sum of indices:",({i},{j}),"is 7. Moreover, its values are=",({nums[i]},{nums[j]}))