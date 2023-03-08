import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

text_0 = pd.read_csv("../input/emg-4/0.csv", header=None)
text_1 = pd.read_csv("../input/emg-4/1.csv", header=None)
text_2 = pd.read_csv("../input/emg-4/2.csv", header=None)
text_3 = pd.read_csv("../input/emg-4/3.csv", header=None)

text_0.head()
