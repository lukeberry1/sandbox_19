ages_dict = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}

new_one = {name: age for name, in ages_dict.items() if age < 18}
print(new_one)