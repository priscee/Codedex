import numpy as np

passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

#==What is the shape of this array?==#
print(passengers.shape)

#==What is the average age of the passengers?==#
print(np.average(passengers, axis = 0)[3])

#==What is the passenger number of the oldest passenger?==#

#find index row with max age
oldest_passenger = np.argmax(passengers[:, 3])

#passenger number of oldest passenger
oldest_passenger_number = passengers[oldest_passenger, 0]
print(oldest_passenger_number)

#==Who is the youngest?==#

#find index row with max age
youngest_passenger = np.argmin(passengers[:, 3])

#passenger number of youngest passenger
youngest_passenger_number = passengers[youngest_passenger, 0]
print(youngest_passenger_number)

#==What is the percentage of folks that survived?==#

#count number of passgeners who survived
survived_folks = np.sum(passengers[:, 1] == 1)

#count total number of passengers
total_passengers = len(passengers)

# % of passengers who survived
percentage_survived = (survived_folks / total_passengers) * 100

print(percentage_survived)

#==What is the percentage of the folks that survived based on their passenger class?==#

#count total number of passengers per class
total_passengers_per_class = np.bincount(passengers[:, 2])

#count number of passengers survived per class
survived_per_class = np.bincount(passengers[passengers[:, 1] == 1, 2])

# % of passengers survived per class
percentage_survived_per_class = np.zeros_like(total_passengers_per_class, dtype=float)
nonzero_mask = total_passengers_per_class != 0
percentage_survived_per_class[nonzero_mask] = (survived_per_class[nonzero_mask] / total_passengers_per_class[nonzero_mask])

#print result
for i, percentage in enumerate(percentage_survived_per_class[1:], start=1):
    print("Passenger class {}: {:.2f}%".format(i, percentage))