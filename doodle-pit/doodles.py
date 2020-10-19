import pandas as pd

cars = {'Brand': ['Honda Civic', 'Toyota Corolla', 'Ford Focus', 'Audi A4'],
        'Price': [22000, 25000, 27000, 35000]
        }

df = pd.DataFrame(cars, columns=['Brand', 'Price'])
df.to_csv(r'C:\Users\pauld\OneDrive\Documents\GitHub\fantasy-leagues\test_csv.csv', index=False, header=True)
print(df)

