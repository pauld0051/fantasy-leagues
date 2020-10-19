<<<<<<< HEAD
import pandas as pd

cars = {'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
        'Price': [22000, 25000, 27000, 35000]
        }

df = pd.DataFrame(cars, columns=['Brand', 'Price'])
df.to_csv(r'C:\Users\pauld\OneDrive\Documents\GitHub\fantasy-leagues\test_csv.csv', index=False, header=True)
print(df)

=======
import numpy as np

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]

C = np.array(cvalues)
print(C)
>>>>>>> 31d9a87f673e400cb0e6eb76f1b703955e11a587
