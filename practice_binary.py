num=[1,2,3,4,5,6,7,8,9,10]
target = 8
ans=''
for i in range(len(num)):
    if num[i]==target:
        abc=ans.append(i)
        if abc != '':
            print("The index of", target, "in num is= ", i)
        else:
            print(target," is not availabe in array")