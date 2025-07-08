#multiplicatio table printer: print the multiplication table for given number upto 10, but skip the fifth itertation.
number=3
for i in range (1, 11):
    if i == 5:
        continue  # Skip the fifth iteration
    #print(f"{number} * {i} = {number * i}")
    print(number,'x', i, '=', number * i)i

   