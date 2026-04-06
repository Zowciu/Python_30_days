# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]



print(f"Length of companies: {len(it_companies)}")

it_companies.add("Twitter")

print(f"Length of companies: {len(it_companies)}")
it_companies.update({"Verocel", "Wisk"})

print(f"Length of companies: {len(it_companies)}")
print(it_companies)

it_companies.remove("Wisk")
print(f"Length of companies: {len(it_companies)}")
print(it_companies)

it_companies.discard("Wisk")





print(A.issubset(B))

print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)

print(AB)
print(BA)

print(A.symmetric_difference(B))

age_set = set(age)

print(f"List age length: {len(age)} | Set age length: {len(age_set)}")

print(age)
print(age_set)

sentence = "I am a teacher and I love to inspire and teach people"
words_list = sentence.split(" ")
print(words_list)

unique_words = set(words_list)
print(unique_words)
print(len(unique_words))