def centered_average(nums):
  length = len(nums)
  sort_l = sorted(nums) 
  if length %2 !=0:
    return sort_l[(length //2)]
  else: 
    x = sort_l[(length // 2)-1]
    y = sort_l[(length // 2)]
    return int((x+y)*0.5)