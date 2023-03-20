def subsetsum(numbers: list, target) -> bool:
    lenght_sum = len(numbers)
    for i in range(lenght_sum):
        
   

# def bubbleSort(array): # n*n
#     swapped = True
#     length_to_loop = len(array)
#     while swapped:
#         swapped=False
#         length_to_loop -= 1
#         for i in range(length_to_loop):
#             if array[i] > array[i+1]:
#                 temp = array[i+1]
#                 array[i+1] = array[i]
#                 array[i] = temp
#                 swapped=True
# array = [6, 5, 12, 10, 9, 1]
# bubbleSort(array)
# print(array)

nums = [12, -7, 20, 1, 4, -10, -1]

subsetsum(nums, 1) # False
subsetsum(nums, 2) # True: 12,  -10
subsetsum(nums, 3) # True: 4,  -1
subsetsum(nums, 4) # False
