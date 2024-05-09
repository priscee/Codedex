import numpy as np

month_results = np.array([56, 100, 33, 0, 45, 45, 46, 34, 89, 180, 60, 45, 45, 44, 46, 45, 0, 0, 15, 90, 301, 197, 20, 60, 45, 45, 42, 45])

print(month_results.shape)
#output: (28,)

new_month_results = month_results.reshape(4, 7)

print(new_month_results)
'''
output: [[ 56 100  33   0  45  45  46]
 [ 34  89 180  60  45  45  44]
 [ 46  45   0   0  15  90 301]
 [197  20  60  45  45  42  45]]
'''