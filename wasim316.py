cities=["Bhopal",
        'Mumbai',
        'Shoharat Garh',
        'Bikaner',
        'Bhopal',
        'Ahmedabaad',
        'Lucknow',
        'Siddharthnagar',
        'Amethi']
d={}
for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    name=[]
    for city in cities:
        if city.startswith(alpha):
            name.append(city)
    if name:
        d[alpha]=name
print(d)