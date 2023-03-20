nums = [6, 4, 100, 5, 200, 2, 3]

def longest(nums: list) -> int:
    nums = sorted(nums)
    biggest_sql = 0
    corrent_sql = 1

    for i in range(len(nums)-1):
        if (nums[i+1] - nums[i]==1):
            corrent_sql += 1
        else:
            if corrent_sql > biggest_sql:
                biggest_sql = corrent_sql
            corrent_sql = 1
    
    return biggest_sql


print(longest(nums))