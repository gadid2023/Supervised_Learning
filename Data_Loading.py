import pandas as pd

class Data_Loading:
    data = pd.read_csv('sales_data.csv')
    X = data.drop(columns=['Sales'])
    Y = data['Sales']

    print(Y.head())
    