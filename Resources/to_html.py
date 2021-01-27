import pandas as pd

df = pd.read_csv(r"Homework\Instructions\Resources\cities.csv")

text_file = open(r"Homework\Instructions\Resources\table.txt", "w")

text_file.write(df.to_html())

text_file.close()