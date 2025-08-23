the_list = input("Enter numbers separated by spaces: ")

nums = [int(x) for x in the_list.split()]

total = 0
for num in nums:
    total += num

print("Sum:", total)