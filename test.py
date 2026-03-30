
def list():
    list = []
    print(len(list))
    list = [1, 2, 3, 4, 5]
    print(len(list))

    print(f"first {list[0]} | mid: {list[(len(list)//2)]} | last: {list[len(list)-1]}")

    mixed_data_types = ["Szymon", 26, 184, "alone", "Kasprowicza 12"]

    for i in range(len(mixed_data_types)):
        print(mixed_data_types[i])


    it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

    for i in range(len(it_companies)):
        print(it_companies[i], end=", ")

    print()
    print(f"Number of companies: {len(it_companies)}")

    print(f"first: {it_companies[0]} | mid: {it_companies[(len(it_companies)//2)]} | last: {it_companies[len(it_companies)-1]}")

    it_companies.append("Verocel")

    for i in range(len(it_companies)):
        print(it_companies[i], end=", ")




    it_companies.insert((len(it_companies)//2), "Boeing")

    print()
    print()
    for i in range(len(it_companies)):
        print(it_companies[i], end=", ")

    print()

    it_companies = [x.upper() if x == "Verocel" else x for x in it_companies]


    print((it_companies))

    x = "#".join(it_companies)
    print(x)

    if "Boeing" in it_companies:
        print("Tak")
    else:
        print("Nie")

    it_companies.sort()

    print(it_companies)

    it_companies.reverse()

    print(it_companies)

    first3 = it_companies[:3]
    last3 = it_companies[-3:]

    print(first3)
    print(last3)

    it_companies.append("asd")

    n = len(it_companies)

    print(it_companies)

    middle = ""
    if n % 2 == 0:
        print("tutaj")
        middle = it_companies[n//2-1:n//2+1]
    else:
        middle = it_companies[n//2] 

    print(middle)

    print(it_companies)

    it_companies.pop(0)

    print(it_companies)

    it_companies.pop()

    print(it_companies)

    it_removed = it_companies.clear()

    print(it_removed)

    del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

index = full_stack.index("Redux")
full_stack[index+1:index+1] = ["Python", "SQL"]

print(full_stack)

ages = [19, 22, 19, 23, 20, 25, 26, 27, 25, 24]

ages.sort()

print(ages)
print(ages[0])
print(ages[-1])

ages.insert(0, 18)
ages.insert(ages[-1], 29)

print(ages)

median = 0
if len(ages) % 2 == 0:
    median = (ages[len(ages)//2-1] + ages[len(ages)//2]) / 2
else:
    median = ages[len(ages)//2]

print(median)

avrg = sum(ages) / len(ages)
print(f"Average: {avrg}")

print(f"Range: {ages[-1] - ages[0]}")

print(abs(ages[0]-avrg))
print(abs(ages[-1]-avrg))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

countries_1 = []
countries_2 = []

if len(countries) % 2 == 0:
    print(countries[len(countries)//2 -1])
    print(countries[len(countries)//2])
    
    countries_1 = countries[:len(countries)//2]
    countries_2 = countries[len(countries)//2:]
else:
    print(countries[len(countries)//2])
    countries_1 = countries[:len(countries)//2+1]
    countries_2 = countries[len(countries)//2+1:]

print(len(countries_1))
print(len(countries_2))

print(countries_1)
print()
print(countries_2)