number_of_connections = int(input())


class City:
    start = ""
    end = ""
    dist = int(0)

    def __init__(self, start, end, dist):
        self.start = start
        self.end = end
        self.dist = dist


arr = []
max_dist = int(-1)
max_idx = int(0)

for i in range(number_of_connections):
    city1 = input()
    city2 = input()
    dis = int(input())

    arr.append(City(city1, city2, dis))

    if dis > max_dist:
        max_dist = dis
        max_idx = i


# for i in range(len(arr)):
#     print(i)
#     print(arr[i].start)
#     print(arr[i].end)
#     print(arr[i].dist)


visiting_cities = []
res_dist = 0


visiting_cities.append(arr[max_idx].end)
# from starting index to right
for i in range(max_idx+1, len(arr)):
    # print(i)
    res_dist += arr[i].dist
    visiting_cities.append(arr[i].end)


# from left to starting index
for i in range(0, max_idx):
    # print(i)
    res_dist += arr[i].dist
    visiting_cities.append(arr[i].end)


print(res_dist)
print(visiting_cities)



"""
input:
20
Rabat
Sueca
1063
Sueca
Rudow
2656
Rudow
Mosu
1352
Mosu
Le Plessis Trevise
1841
Le Plessis Trevise
Kang Dong
61
Kang Dong
Nezahualcóyotl
1634
Nezahualcóyotl
Lindenwold
151
Lindenwold
Queanbeyan
285
Queanbeyan
Saint Chamond
146
Saint Chamond
Cheektowaga
11
Cheektowaga
Tirupati
380
Tirupati
Snezhinsk
2547
Snezhinsk
Glazov
2524
Glazov
Gaoyou
97
Gaoyou
Nola
6999
Nola
Rutigliano
63
Rutigliano
Colombo
105
Colombo
Meckenheim
244
Meckenheim
Hamburg
502
Hamburg
Rabat
30

output:
15692
['Nola', 'Rutigliano', 'Colombo', 'Meckenheim', 'Hamburg', 'Rabat', 'Sueca', 'Rudow', 'Mosu', 'Le Plessis Trevise', 'Kang Dong', 'Nezahualcóyotl', 'Lindenwold', 'Queanbeyan', 'Saint Chamond', 'Cheektowaga', 'Tirupati', 'Snezhinsk', 'Glazov', 'Gaoyou']

"""