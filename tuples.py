empty_tuple = ()
print(empty_tuple)

men = ("Szymon",  "Jarek", "Heniu")
women = ("Basia", "Mariola", "Ela")

siblings = men + women
print(siblings)
print(f"Number of siblings: {len(siblings)}")

family_members = siblings + ("Mom" , "Dad")
print(family_members)

siblings_2 = family_members[0:-2]
parents = family_members[-2:]
print(siblings_2)
print(parents)


fruits = ("apple", "banana", "orange", "grape", "mango")
vegetables = ("carrot", "broccoli", "tomato", "cucumber", "pepper")
animal_products = ("milk", "cheese", "eggs", "butter", "honey")

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

print(len(food_stuff_lt))

mid = len(food_stuff_lt)//2

if len(food_stuff_lt) % 2 == 0:
    food_stuff_lt = food_stuff_lt[:mid-1] + food_stuff_lt[mid+1:]
else:
    food_stuff_lt = food_stuff_lt[:mid] + food_stuff_lt[mid+1:]

print(food_stuff_lt)

food_stuff_lt = food_stuff_lt[3:-3]

print(food_stuff_lt)

del food_stuff_tp
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in nordic_countries:
    print("Proste że jest Estonia")
elif "Iceland" in nordic_countries:
    print("Proste że jest Islandia")
else:
    print("No nic ni ma")