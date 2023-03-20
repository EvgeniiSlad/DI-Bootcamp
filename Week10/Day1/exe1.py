nums = [12, -7, 20, 1, 4, -10, -1]

def subsetsum(nums , target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j] == target):
                return True
    return False

print(subsetsum(nums, 32)) # True

print(subsetsum(nums, 1)) # False
print(subsetsum(nums, 2)) # True: 12,  -10
print(subsetsum(nums, 3)) # True: 4,  -1
print(subsetsum(nums, 4)) # False