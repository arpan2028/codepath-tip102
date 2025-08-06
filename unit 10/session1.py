# session 19

flights = {"JFK": ["LAX", "DFW"],
           "LAX": ["JFK"],
           "DFW": ["ATL", "JFK"],
           "ATL": ["DFW"]}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

def bidirectional_flights(flights):
    # iterate through flights
    for i in range(len(flights)):
        for j in


    # iterate through all elements inindex we are checking
            #i              j
flights1 = [[1, 2], [0], [0, 3], [2]]
            #i      j
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

def get_adj_dict(flights):
    # initialize adj dict
    adj_dict = {}
    # iterate through the flights
    for a, b in flights:
    #   get flights[i] = [a, b]
    #   for key a, add b to value list
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict [a] = [b]
    #   for key b, add a to value list
        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]
    # return the adj_dict
    return adj_dict

# flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'],
#             ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
# print(get_adj_dict(flights))