number_of_connections = int(input())

city_identity = {}
connections = {}
costs = {}
city_number = 0


for i in range(number_of_connections):
    city1 = input()
    city2 = input()

    if city1 not in city_identity:
        city_identity[city1] = city_number
        connections[city_number] = []
        costs[city_number] = []
        city_number += 1

    if city2 not in city_identity:
        city_identity[city2] = city_number
        connections[city_number] = []
        costs[city_number] = []
        city_number += 1

    connections[city_identity[city1]].append(city_identity[city2])
    connections[city_identity[city2]].append(city_identity[city1])

    distance = int(input())
    costs[city_identity[city1]].append(distance)
    costs[city_identity[city2]].append(distance)

# print(connections)
# print(costs)
visit_All = (1 << city_number)-1
memo = []

for i in range(pow(2, city_number)):
    temp = []
    for j in range(city_number):
        temp.append(int(-1))
    memo.append(temp)


def sol(mask, pos):
    if mask == visit_All:
        return 0

    if memo[mask][pos] != -1:
        return memo[mask][pos]

    min_dis = int(1e9 + 7)
    for x in range(len(connections[pos])):
        city = connections[pos][x]
        if mask & (1 << city) == 0:
            dis = costs[pos][x] + sol(mask | (1 << city), city)
            min_dis = min(min_dis, dis)

    memo[mask][pos] = min_dis
    return memo[mask][pos]


print(sol(1, 0))

"""
input:
6
a
b
20
a
c
42
b
c
30
b
d
34
c
d
10
d
a
25
output:
60

"""
