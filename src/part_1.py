# LIST COMPREHENSION

# Assignment: create a new list with only odd numbers from arr = [1, 2, 3, 4, 5]

arr = [1, 2, 3, 4, 5]

# junior
new_arr = []
for e in arr:
    if e % 2 == 1:
        new_arr.append(e)

# senior
new_arr = [e for e in arr if e % 2 == 1]
