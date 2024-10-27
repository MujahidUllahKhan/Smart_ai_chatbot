num=[1,2,3,4,5,6,7,8,9]
l=0
r=len(num)-1
while l<= r:
    mid=(l+r)//2
    result = guess(mid)
    if result == 0:
        return mid
    elif result == -1:
        r = mid -1
    else:
        l= mid+1