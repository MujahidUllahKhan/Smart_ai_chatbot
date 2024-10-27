  num=[1,2,3,4,5,6,7,8,9]
  target=9
  l=0
  r= len(num)-1
  while l<=r:
        mid=(l+r)//2
      if target==num[mid]:
          abc=mid
      elif target < num[mid]:
          r=mid-1
      else:
          l=mid+1
print(abc)