import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Daten laden
data = pd.read_csv ("data/auto-mpg-training-data.csv", sep = ";")

print (data)

# Daten mischen
data = data.sample (frac=1)

# y erstellen
y_variable = data ["mpg"]

# x erstellen
x_variables = data.loc [:, data.columns != "mpg"]


# Split in Test und Trainingsdaten
x_train, x_test, y_train, y_test = train_test_split(x_variables, y_variable, test_size = 0.2)

# Modelle trainieren
regressor = LinearRegression()
regressor = regressor.fit (x_train, y_train)

y_pred = regressor.predict(x_test)

#Prädiktion ausgeben
print (y_pred)

# Modell abspeichern
file_to_write = open("data/models/regression.pickle", "wb")
pickle.dump(regressor, file_to_write)
