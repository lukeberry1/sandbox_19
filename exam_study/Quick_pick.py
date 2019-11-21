from random import randint

number_of_picks = int(input("How many quick picks:"))

for number in range(number_of_picks):
    quick_pick = []
    for i in range(6):
        quick_pick.append(randint(1,45))
    print(" ".join("{:2}".format(number) for number in quick_pick))