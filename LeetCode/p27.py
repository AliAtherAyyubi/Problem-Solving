

def removeElement(nums,val):
    k=0
    # nums.sort()
    for i in range(len(nums)):
        if nums[i] != val :
            nums[k]=nums[i]
            k=k+1
    print(k)     
    return nums

if __name__ == '__main__':

    print(removeElement([3,2,2,3,4,4],3))