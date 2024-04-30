import pandas as pd
import pickle
import numpy as np

# Modell laden
file_to_open = open("data/models/regression.pickle", "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close ()

# Data laden für Prädiktion
prediction_data = pd.read_csv("data/auto-ohne-mpg.csv", sep=";")

print (trained_model.predict(prediction_data))

# Ergebnisse in csv speichern
#save_predictions = open("data/predictions.csv", "w")
#save_predictions.write (
 #   np.savetxt("data/predictions.csv", save_predictions, delimeter= ","))
