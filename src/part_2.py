# DICTIONARY COMPREHENSION

# Assignment: From a dictionary of names and ages, create a new dictionary with only the names of people who are older than 18

people = {"Alice": 17, "Bob": 20, "Carol": 15, "Dave": 22}

# junior
adults = {}
for name, age in people.items():
    if age >= 18:
        adults[name] = age

# senior
adults = {name: age for name, age in people.items() if age >= 18}
