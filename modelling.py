from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import pandas as pd
import pickle
import os


def model_making():
    print("moddeling called")
    filename = "dataframe.csv"
    current_path = Path(os.path.dirname(os.path.abspath("__file__")))
    filename = "online_shoppers_intention.csv"
    df = pd.read_csv(os.path.join(current_path, filename))

    df = pd.get_dummies(df, columns=["VisitorType", "Month"])
    df['Weekend'] = df['Weekend'].astype(int)
    df['Revenue'] = df['Revenue'].astype(int)

    X = df.drop('Revenue', axis=1)
    Y = df['Revenue']



    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    randomforestclassifier_model = RandomForestClassifier(n_estimators=50, max_depth=15, random_state=12)
    randomforestclassifier_model.fit(x_train, y_train)

    filename = "LLM.pickle"
    with open(os.path.join(current_path, filename), 'wb') as file:
        pickle.dump(randomforestclassifier_model, file)




