def sum67(nums):
  for i in range(len(nums)):
    if nums[i] == 6:
      position_of_7 = nums.index(7,i)
      if position_of_7 != i + 1:
        for j in range(len(nums[i:position_of_7+1])):
          nums[i+j] =0
      else:
        nums[i] = 0
        nums[i+1] = 0
  return sum(nums)

print(sum67([1, 2, 2])) #5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7,2])) # 4
print(sum67([2, 7, 6, 2, 6, 7, 2, 7])) #18