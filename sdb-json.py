import requests
import numpy as np

# Event id
id = 1032723
# apiKey (only 1 works currently)
apiKey = 1

# the 'f' here allows you to pass variables, such as id, into a string inside {}
r = requests.get(
    f'https://www.thesportsdb.com/api/v1/json/{apiKey}/lookupeventstats.php?id={id}')

arr = np.array([r.json()])

#print(arr)

r2 = requests.get(
    f'https://www.thesportsdb.com/api/v1/json/{apiKey}/lookupevent.php?id={id}')

arr2 = np.array([r2.json()])

print(arr2)
