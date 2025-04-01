
# return the index of target value 
def searchInsert(nums, target):
    low=0
    high= len(nums)-1
    mid=0
    # print(high,mid)
    while low<=high:
        mid=int((low+high)/2)
        print(low,high,mid)

        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return low 
    # if target not in nums:
    #     if target>nums[high]:
    #         nums.insert(high+1,target)
    #         return nums.index(target)
    #     else:
              

        
    # return nums.index(target)



ls=[1,3,4,6]

print(searchInsert(ls,2))
# print(searchInsert(ls,3))
        
# print(ls)