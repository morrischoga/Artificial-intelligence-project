
from pathlib import Path
from api import save_data
import numpy as np
import pickle
import json

import os


def pred(x):
    current_path = Path(os.path.dirname(os.path.abspath("__file__")))
    filename = "LLM.pickle"
    with open(os.path.join(current_path, filename), 'rb') as model:
        model = pickle.load(model)

    proba = model.predict_proba(x)
    proba = "{:.2f}".format(np.max(proba))
    prediction = model.predict(x)
    return json.dumps({str(prediction[0]):proba})
