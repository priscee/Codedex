import numpy as np

steps_taken = np.array([3384, 6560, 5026, 162, 208, 192, 2767])

print(np.min(steps_taken))
#output: 162

print(np.max(steps_taken))
#output: 6560

print(np.sum(steps_taken))
#output: 18299

print(np.average(steps_taken))
#output: 2614.1428571428573