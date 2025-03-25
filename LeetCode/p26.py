

def removeDuplicates(nums):

    for i in range(len(nums)-1):
        x= nums[i]
        # j=i+1
        k=0
        for j in range(len(nums)-1):
            # y= nums[j+1]
            if x==nums[j+1]:
                nums[j+1]='_'
            
           
    return nums

if __name__ == '__main__':
    print(removeDuplicates([1,1,2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))