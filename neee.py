def twosum(nums,target):
 results = []  # List to store the pairs of indices
  for i in range (len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i] + nums[j] == target:
            results.append((i, j))
return results
# Call the function and print the result
result = twosum([1, 6, 3, 4], 7)

# Print indices and corresponding values
for i, j in result:
    print(f"Indices: ({i}, {j}) -> Values: ({nums[i]}, {nums[j]})")