import numpy
import pandas as pd

file_name = r"C:\Users\leo.martinez\OneDrive\Desktop\School\DNA_sequence_classification_prj\data_files\promoters.data"

df = pd.read_csv(file_name, header=None, names = ["Class", "ID", "Sequence"], skipinitialspace=True)
print(df)
print(df["ID"])
print(df["Class"])

