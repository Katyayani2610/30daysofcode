number=[1,2,3,4,5,6,7,66 -1,-2,-3,-4,-5,-6]
positive_number_count = 0
for num in number:
    if num > 0:
        positive_number_count += 1
print("final count of positive numbers:", positive_number_count)