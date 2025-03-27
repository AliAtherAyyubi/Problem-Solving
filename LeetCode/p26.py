

def removeDuplicates(nums):
    k=1

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k=k+1
    print(k)     
    return nums

if __name__ == '__main__':
    print(removeDuplicates([1,1,2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))