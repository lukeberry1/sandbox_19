people_age = {"Bill": 21, "Jane": 34, "Jack": 56}

name = input("Name:")
age = int(input("Age:"))

people_age[name] = people_age.get(name, age)

for name in people_age:
    print("{:<30} {}".format(name, people_age[name]))