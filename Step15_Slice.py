

nums = [10, 20, 30, 40, 50]

print(nums[0:])
print(nums[1:])
print(nums[2:])
print(nums[3:])
print(nums[4:])
print(nums[5:])

print("------------------------------------------------------")

print(nums[:5])
print(nums[:4])
print(nums[:3])
print(nums[:2])
print(nums[:1])
print(nums[:0])

print("------------------------------------------------------")
# nums[::n] index를 n만큼 증가 ex) 0 - > 0 + n -> 0 + n + n
print(nums[::1]) 
print(nums[::2])
print(nums[::3])