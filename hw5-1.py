# Ryan Lugo: RJL 10/26/21

import random as r

# Question 1
r.randint(31,59)

# Question 2
r.randint(3,74)

# Question 3
r.randint(20,30)

# Question 4
r.randint(0,8)

# Question 5
r.randint(0,20)

# Question 6
table = ['cat','dog','sheep','cow','chicken','pig']
animal_chosen = r.choice(table)
print(animal_chosen,"Was chosen")

# Question 7
random_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(r.choices(random_10, k=4))

# Question 8
random_5 = [1,2,3,4,5]
print(r.choices(random_5, k=5))

# Question 9
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
card_chosen = r.choice(cards)
print(card_chosen,"was the card # chosen.")

# Question 10
r.seed(1942)
r.randint(1,1000)
