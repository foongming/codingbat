def has22(nums):
  if nums:
    for i in range(len(nums)):
      if i != len(nums)-1:
        if nums[i] == 2 and nums[i+1] == 2:
          return True
      else: 
        return False 
  else:
    return False