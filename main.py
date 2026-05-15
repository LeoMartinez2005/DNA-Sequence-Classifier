import numpy
import numpy as np
import pandas
import pandas as pd
import sys


file_name = r"C:\Users\leo.martinez\OneDrive\Desktop\School\DNA_sequence_classification_prj\data_files\promoters.data"

data = pd.read_csv(file_name, header=None, names = ["Class", "ID", "Sequence"], skipinitialspace=True)
print(data)
print(data["ID"])
print(data["Class"])

data.head()
data.to_csv("promoter.csv")
data.tail()

classes = data.loc[:, 'Class']
print(classes[:5])

sequences = list(data.loc[:, 'Sequence'])

dataset = {}

for i, seq in enumerate(sequences):
    nucleotides = list(seq)
    nucleotides = [x for x in nucleotides if x != '\t']
    nucleotides.append(classes[i])
    dataset[i] = nucleotides
print(dataset[0])

dframe = pd.DataFrame(dataset)
dframe.head()
