# 4.3
nums = range(1, 21)
for counting in nums:
    print(counting)

# 4.4 - 4.5

# for nums in range(1, 1000001):
#     print(nums)

onemil = list(range(1, 1000001))
print(f"Min number is: {min(onemil)}")
print(f"Max number is: {max(onemil)}")
print(f"Total Sum is: {sum(onemil)}")

# 4.6

for odd in range(1, 21, 2):
    print(odd)

# 4.7

nums = list(range(3,31))
print(nums)

for multiples in nums:
    print(3*multiples)

# 4.8

for cube in range(1, 11):
    print(f"Cube numbers: {cube**3}")

# 4.9

cubenums = [cubenum**3 for cubenum in range(1,11)]
print(f"expert: {cubenums}")
