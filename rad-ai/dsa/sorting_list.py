#bubble sort

theList = [5,2,4,1,3,5,1]

def sort(nums):
    l = len(nums)

    for a in range(l):
        for b in range(0,l-a-1):
            if nums[b] > nums[b + 1]:
                nums[b], nums[b + 1] = nums[b + 1], nums[b]
    return nums


sort(theList)

print(theList)

