"""
lab-oefening: list
2019-012 smart-city, bron: The Quick Python Book, 3rd ed, Manning

"""
temperatures = []
lab_file = 'lab_temp.txt'  # list of temperature data
with open(lab_file) as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print('Aantal ingelezen temperaturen:', len(temperatures))  # 828

# uitwerking
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)
# we'll need to sort to get the median temperature
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))
