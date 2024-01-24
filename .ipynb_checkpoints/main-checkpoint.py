import pandas as pd
import os
from pathlib import Path



current_path = Path(os.path.dirname(os.path.abspath("__file__")))
filename = "online_shoppers_intention.csv"

data = pd.read_csv(os.path.join(current_path,filename))
print(data.head(12))
# print(data.median)


